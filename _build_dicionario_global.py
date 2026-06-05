#!/usr/bin/env python3
"""Consolida DICIONARIO.md das 12 disciplinas em DICIONARIO_GLOBAL.md."""
from __future__ import annotations

import re
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BASE = ROOT / "01 Básico em Teologia"
OUT_DIR = ROOT / "90_Knowledge_Base"
OUT_FILE = OUT_DIR / "DICIONARIO_GLOBAL.md"

DISCIPLINES = [
    ("01", "Introdução a Teologia"),
    ("02", "Métodos de Estudos Bíblicos"),
    ("03", "Homilética"),
    ("04", "Arqueologia e Geografia 1"),
    ("05", "Arqueologia e Geografia 2"),
    ("06", "Pentateuco"),
    ("07", "Doutrinas Bíblicas do Velho Testamento"),
    ("08", "Teologia do Novo Testamento"),
    ("09", "Livros Poéticos"),
    ("10", "Hermenêutica"),
    ("11", "Os Evangelhos"),
    ("12", "Heresiologia"),
]

CATEGORIAS = {
    "Pessoa",
    "Lugar",
    "Doutrina",
    "Conceito",
    "Evento",
    "Livro Bíblico",
    "Heresia",
    "Seita",
    "Instituição",
    "Período Histórico",
    "Termo Grego",
    "Termo Hebraico",
}

TIPO_MAP = {
    "personagem": "Pessoa",
    "pessoa": "Pessoa",
    "cidade": "Lugar",
    "local": "Lugar",
    "lugar": "Lugar",
    "conceito": "Conceito",
    "doutrina": "Doutrina",
    "evento": "Evento",
    "heresia": "Heresia",
    "seita": "Seita",
    "livro": "Livro Bíblico",
    "instituicao": "Instituição",
    "instituição": "Instituição",
    "periodo": "Período Histórico",
    "período": "Período Histórico",
    "periodo historico": "Período Histórico",
}

# Correções ortográficas e sinônimos (auditoria Fase 1B / RELATORIO_GERAL)
CANONICAL_ALIASES: dict[str, str] = {
    "guinoticismo": "Gnosticismo",
    "gnosticismo": "Gnosticismo",
    "instituto teologico renacer": "Instituto Teológico Renacer",
    "instituto teologico renace": "Instituto Teológico Renacer",
    "renacer instituto teologico": "Instituto Teológico Renacer",
    "instituto renacer": "Instituto Teológico Renacer",
    "instituto biblico renacer": "Instituto Teológico Renacer",
    "pastor tiago dominguez": "Pastor Tiago Domínguez",
    "tiago dominguez": "Pastor Tiago Domínguez",
    "tiago domingus": "Pastor Tiago Domínguez",
    "pastor carvalho junior": "Pastor Carvalho Júnior",
    "carvalho junho": "Pastor Carvalho Júnior",
    "carvalho junior": "Pastor Carvalho Júnior",
    "coelhada": "Goel",
    "vingador de sangue": "Goel",
    "aemia paputoliva": "Aelia Capitolina",
    "jerusalem romana": "Aelia Capitolina",
    "imeneutica": "Hermenêutica",
    "exigencia": "Exegese",
    "gensabele": "Jezabel",
    "atanasio": "Atanásio de Alexandria",
    "renaceno": "Instituto Teológico Renacer",
    "renaciano": "Instituto Teológico Renacer",
    "renasem": "Instituto Teológico Renacer",
}

LIVROS_BIBLICOS = {
    "genesis", "exodo", "levitico", "numeros", "deuteronomio",
    "josue", "juizes", "rute", "samuel", "reis", "cronicas",
    "esdras", "neemias", "ester", "jo", "salmos", "proverbios",
    "eclesiastes", "cantares", "isaias", "jeremias", "lamentacoes",
    "ezequiel", "daniel", "oseias", "joel", "amos", "obadias",
    "jonas", "miqueias", "naum", "habacuque", "sofonias", "ageu",
    "zacarias", "malaquias", "mateus", "marcos", "lucas", "joao",
    "atos", "romanos", "corintios", "galatas", "efesios", "filipenses",
    "colossenses", "tessalonicenses", "timoteo", "tito", "filemom",
    "hebreus", "tiago", "pedro", "judas", "apocalipse",
}

GREEK_TERMS = {
    "euangelion", "theopneustos", "kenosis", "anastasis", "epilysken",
    "sophia", "poietai", "akroatai", "haireses", "korban", "exahemeron",
    "hamartia", "logos", "anastasis",
}
HEBREW_TERMS = {
    "goel", "bara", "torah", "tora", "torá", "panah", "shemen", "megillot",
    "shalom", "hesed", "ruach", "nephesh",
}
GREEK_MARKER = re.compile(r"termo grego|em grego|\(grego\)", re.I)
HEBREW_MARKER = re.compile(r"termo hebraico|em hebraico|hebraico para|\(hebraico\)", re.I)
HERESY_TITLES = {
    "arianismo", "gnosticismo", "pelagianismo", "docetismo", "ebionismo",
    "marcionismo", "nestorianismo", "monofisismo", "sabelianismo",
}


def strip_accents(s: str) -> str:
    return "".join(
        c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn"
    )


def norm_key(title: str) -> str:
    t = strip_accents(title.lower().strip())
    t = re.sub(r"^doutrina\s+(da|de|do|das|dos)\s+", "", t)
    t = re.sub(r"[^a-z0-9]+", " ", t).strip()
    return t


def canonical_key(title: str) -> str:
    k = norm_key(title)
    return norm_key(CANONICAL_ALIASES.get(k, title))


def canonical_title(title: str) -> str:
    k = norm_key(title)
    return CANONICAL_ALIASES.get(k, title)


def normalize_raw(text: str) -> str:
    text = text.lstrip("\ufeff")
    if "\\r\\n" in text:
        text = text.replace("\\r\\n", "\n")
    text = text.replace("\r\n", "\n")
    if "Ã" in text:
        try:
            text = text.encode("latin-1").decode("utf-8")
        except (UnicodeEncodeError, UnicodeDecodeError):
            pass
    return text


def read_disc_file(code: str, filename: str) -> str | None:
    for folder in BASE.iterdir():
        if folder.is_dir() and folder.name.startswith(f"{code} "):
            p = folder / filename
            if p.exists():
                return normalize_raw(p.read_text(encoding="utf-8", errors="replace"))
    return None


def parse_field(body: str, field: str) -> str:
    m = re.search(rf"-\s+\*\*{re.escape(field)}\*\*:\s*(.+)", body)
    return m.group(1).strip() if m else ""


def parse_h3_blocks(text: str) -> list[tuple[str, str]]:
    blocks: list[tuple[str, str]] = []
    for part in re.split(r"\n(?=### )", text):
        part = part.strip()
        if not part.startswith("### "):
            continue
        lines = part.split("\n", 1)
        title = lines[0].replace("### ", "").strip()
        body = lines[1].strip() if len(lines) > 1 else ""
        if title and not title.startswith("#"):
            blocks.append((title, body))
    return blocks


def split_list_field(value: str) -> list[str]:
    if not value or value in ("—", "-", "Não identificado nas fontes analisadas.",
                              "Não identificadas explicitamente nas aulas desta disciplina."):
        return []
    parts = re.split(r"[,;]\s*|\s+/\s+", value)
    out: list[str] = []
    for p in parts:
        p = p.strip().strip(".")
        if p and len(p) > 1:
            out.append(p)
    return out


def infer_categoria(tipo: str, title: str, definicao: str, body: str) -> str:
    t = tipo.lower().strip()
    nk = norm_key(title)
    text = f"{title} {definicao}"

    if t in TIPO_MAP:
        cat = TIPO_MAP[t]
    elif "heresia" in t:
        cat = "Heresia"
    elif "seita" in t:
        cat = "Seita"
    else:
        cat = "Conceito"

    if nk in HERESY_TITLES or re.match(r"^heresia\b", definicao, re.I):
        return "Heresia"
    if nk in LIVROS_BIBLICOS or re.search(r"\blivro\b", definicao, re.I):
        return "Livro Bíblico"
    if re.search(r"doutrina\s+(da|de|do)", title, re.I):
        return "Doutrina"
    if "instituto" in nk or "renacer" in nk:
        return "Instituição"
    if nk in GREEK_TERMS or GREEK_MARKER.search(text):
        return "Termo Grego"
    if nk in HEBREW_TERMS or HEBREW_MARKER.search(text):
        return "Termo Hebraico"
    return cat


def pick_title(titles: list[str]) -> str:
    canon = [canonical_title(t) for t in titles]
    unique = list(dict.fromkeys(canon))
    return max(unique, key=len)


def merge_texts(parts: list[str]) -> str:
    seen: set[str] = set()
    merged: list[str] = []
    for p in parts:
        p = p.strip()
        if not p:
            continue
        pk = norm_key(p)
        if pk not in seen:
            seen.add(pk)
            merged.append(p)
    return " ".join(merged)


def build_verse_index() -> dict[str, set[str]]:
    index: dict[str, set[str]] = defaultdict(set)
    for code, _ in DISCIPLINES:
        ver = read_disc_file(code, "VERSICULOS.md")
        if not ver:
            continue
        for title, body in parse_h3_blocks(ver):
            refs = {title}
            for field in ("Conceitos relacionados", "Doutrinas relacionadas"):
                for item in split_list_field(parse_field(body, field)):
                    refs.add(item)
            for ref in refs:
                index[norm_key(ref)].add(title)
    return index


def build_doutrina_index() -> dict[str, str]:
    index: dict[str, str] = {}
    for code, _ in DISCIPLINES:
        dout = read_disc_file(code, "DOUTRINAS.md")
        if not dout:
            continue
        for title, body in parse_h3_blocks(dout):
            k = canonical_key(title)
            snippet = parse_field(body, "Definição") or parse_field(body, "Resumo")
            if not snippet:
                lines = [ln.strip() for ln in body.splitlines() if ln.strip() and not ln.startswith("- **")]
                snippet = " ".join(lines[:3])[:500]
            if snippet and (k not in index or len(snippet) > len(index[k])):
                index[k] = snippet
    return index


def build_kb_context_index() -> dict[str, str]:
    index: dict[str, str] = {}
    for code, _ in DISCIPLINES:
        kb = read_disc_file(code, "KB_MASTER.md")
        if not kb:
            continue
        for section in ("CONHECIMENTO FUNDAMENTAL", "PERSONAGENS", "EVENTOS"):
            m = re.search(rf"## {section}[^\n]*\n+([\s\S]+?)(?=\n## |\n# |\Z)", kb, re.I)
            if not m:
                continue
            for line in m.group(1).splitlines():
                bm = re.match(r"^[-\d]+\.\s+\*\*(.+?)\*\*:\s*(.+)$", line.strip())
                if not bm:
                    bm = re.match(r"^-\s+\*\*(.+?)\*\*:\s*(.+)$", line.strip())
                if bm:
                    k = canonical_key(bm.group(1))
                    if k not in index or len(bm.group(2)) > len(index[k]):
                        index[k] = bm.group(2).strip()
    return index


def register_alias(alias_map: dict[str, str], alias: str, canonical: str) -> None:
    ak = norm_key(alias)
    ck = norm_key(canonical)
    if ak and ck:
        alias_map[ak] = ck


def main() -> None:
    entries: dict[str, dict] = {}
    alias_to_canonical: dict[str, str] = {}
    raw_count = 0

    verse_index = build_verse_index()
    doutrina_index = build_doutrina_index()
    kb_index = build_kb_context_index()

    for alias_k, canon_title in CANONICAL_ALIASES.items():
        register_alias(alias_to_canonical, alias_k, canon_title)

    for code, dname in DISCIPLINES:
        source = f"{code} {dname}"
        dic = read_disc_file(code, "DICIONARIO.md")
        if not dic:
            continue
        for title, body in parse_h3_blocks(dic):
            raw_count += 1
            canon_t = canonical_title(title)
            key = canonical_key(title)

            tipo = parse_field(body, "Tipo")
            definicao = parse_field(body, "Definição")
            contexto = parse_field(body, "Contexto na disciplina")
            refs = parse_field(body, "Referências bíblicas relacionadas")
            termos = split_list_field(parse_field(body, "Termos relacionados"))
            sinonimos = split_list_field(parse_field(body, "Palavras-chave equivalentes"))

            register_alias(alias_to_canonical, title, canon_t)
            for s in sinonimos:
                register_alias(alias_to_canonical, s, canon_t)

            if key not in entries:
                entries[key] = {
                    "titles": [],
                    "categorias": [],
                    "definicoes": [],
                    "contextos": [],
                    "disciplinas": [],
                    "versiculos": set(),
                    "termos_rel": set(),
                    "sinonimos": set(),
                    "fontes": [],
                    "raw_hits": 0,
                }

            e = entries[key]
            e["titles"].append(title)
            e["categorias"].append(infer_categoria(tipo, canon_t, definicao, body))
            if definicao:
                e["definicoes"].append(definicao)
            if contexto:
                e["contextos"].append(f"[{source}] {contexto}")
            if source not in e["disciplinas"]:
                e["disciplinas"].append(source)
            for vref in split_list_field(refs) or ([refs] if refs else []):
                parts = split_list_field(vref) or ([vref] if vref else [])
                e["versiculos"].update(parts)
            for vref in verse_index.get(key, set()):
                parts = split_list_field(vref) or ([vref] if vref else [])
                e["versiculos"].update(parts)
            e["termos_rel"].update(termos)
            e["sinonimos"].update(sinonimos)
            e["fontes"].append(f"DICIONARIO.md ({source})")
            e["raw_hits"] += 1

    # Resolver aliases de termos relacionados para chaves canônicas existentes
    all_keys = set(entries.keys())
    for e in entries.values():
        resolved: set[str] = set()
        for t in e["termos_rel"]:
            tk = alias_to_canonical.get(norm_key(t), norm_key(canonical_title(t)))
            if tk in all_keys:
                resolved.add(pick_title(entries[tk]["titles"]))
            else:
                resolved.add(t)
        e["termos_rel"] = resolved

    # Enriquecer com DOUTRINAS e KB_MASTER
    for key, e in entries.items():
        title = pick_title(e["titles"])
        if key in doutrina_index:
            e["definicoes"].append(f"[DOUTRINAS] {doutrina_index[key]}")
            e["fontes"].append("DOUTRINAS.md (correlato)")
        if key in kb_index:
            e["contextos"].append(f"[KB_MASTER] {kb_index[key]}")
            e["fontes"].append("KB_MASTER.md (correlato)")

    # Montar saída
    cat_counter: Counter[str] = Counter()
    disc_counter: Counter[str] = Counter()
    freq_counter: list[tuple[str, int]] = []

    lines: list[str] = [
        "---",
        'nivel: "Básico em Teologia"',
        "disciplinas_total: 12",
        "entradas_brutas: " + str(raw_count),
        f"entradas_unicas: {len(entries)}",
        "versao: 1.0.0",
        "fase: 2",
        "---",
        "",
        "# DICIONÁRIO GLOBAL — Pastor IA",
        "",
        "Consolidação alfabética de todos os termos das doze disciplinas do Curso Básico em Teologia. "
        "Entradas duplicadas foram fundidas por chave normalizada; sinônimos e variações ortográficas "
        "identificadas na auditoria foram unificados. A definição mais completa foi preservada e "
        "enriquecida com `DOUTRINAS.md`, `VERSICULOS.md` e `KB_MASTER.md`.",
        "",
        "## Índice de Disciplinas Fonte",
        "",
    ]
    for code, dname in DISCIPLINES:
        lines.append(f"- **{code}** — {dname}")

    sorted_keys = sorted(entries.keys(), key=lambda k: strip_accents(pick_title(entries[k]["titles"])).lower())

    for key in sorted_keys:
        e = entries[key]
        title = pick_title(e["titles"])
        cat = Counter(e["categorias"]).most_common(1)[0][0]
        cat_counter[cat] += 1

        definicao = merge_texts(e["definicoes"])
        contexto = merge_texts(e["contextos"])
        if contexto and contexto not in definicao:
            definicao_consolidada = f"{definicao} {contexto}".strip()
        else:
            definicao_consolidada = definicao

        disciplinas = "; ".join(sorted(e["disciplinas"]))
        vers_seen: dict[str, str] = {}
        for v in sorted(e["versiculos"], key=lambda x: strip_accents(x).lower()):
            vers_seen.setdefault(norm_key(v), v)
        versiculos = "; ".join(vers_seen.values()) if vers_seen else "—"
        termos_rel = "; ".join(sorted(e["termos_rel"])) if e["termos_rel"] else "—"
        freq = len(e["disciplinas"])
        fontes = "; ".join(dict.fromkeys(e["fontes"]))

        for d in e["disciplinas"]:
            disc_counter[d] += 1
        freq_counter.append((title, freq))

        lines.extend([
            "",
            f"### {title}",
            "",
            f"- **Categoria**: {cat}",
            f"- **Definição Consolidada**: {definicao_consolidada}",
            f"- **Disciplinas Relacionadas**: {disciplinas}",
            f"- **Versículos Relacionados**: {versiculos}",
            f"- **Termos Relacionados**: {termos_rel}",
            f"- **Frequência**: {freq}",
            f"- **Fontes**: {fontes}",
        ])
        if e["sinonimos"]:
            lines.append(f"- **Sinônimos unificados**: {', '.join(sorted(e['sinonimos']))}")

    lines.extend(["", "---", "", "## Estatísticas", ""])
    lines.append(f"- **Total de entradas únicas**: {len(entries)}")
    lines.append(f"- **Entradas brutas processadas**: {raw_count}")
    lines.append(f"- **Entradas fundidas**: {raw_count - len(entries)}")
    lines.append("")
    lines.append("### Quantidade por categoria")
    lines.append("")
    for cat, n in cat_counter.most_common():
        lines.append(f"- **{cat}**: {n}")
    lines.append("")
    lines.append("### Termos mais recorrentes (por disciplinas distintas)")
    lines.append("")
    for title, f in sorted(freq_counter, key=lambda x: (-x[1], strip_accents(x[0]).lower()))[:25]:
        lines.append(f"- **{title}**: {f} disciplina(s)")
    lines.append("")
    lines.append("### Disciplinas mais representadas")
    lines.append("")
    for disc, n in disc_counter.most_common():
        lines.append(f"- **{disc}**: {n} termo(s)")

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    OUT_FILE.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Written: {OUT_FILE}")
    print(f"Raw: {raw_count} | Unique: {len(entries)} | Merged: {raw_count - len(entries)}")
    print("Categories:", dict(cat_counter))


if __name__ == "__main__":
    main()
