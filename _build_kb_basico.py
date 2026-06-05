#!/usr/bin/env python3
"""Consolida artefatos do Curso Básico em KB_BASICO_COMPLETO.md."""
from __future__ import annotations

import re
import unicodedata
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).resolve().parent
BASE = ROOT / "01 Básico em Teologia"
OUT_DIR = ROOT / "90_Knowledge_Base"
OUT_FILE = OUT_DIR / "KB_BASICO_COMPLETO.md"

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

HERMENEUTICS_IDS = {"02", "03", "10"}
GEOGRAPHY_IDS = {"04", "05"}
APOLOGETICS_IDS = {"12"}
CHRISTOLOGY_KEYWORDS = re.compile(
    r"cristo|cristolog|messias|verbo|encarn|trindade|filho de deus|"
    r"preexist|kenosis|expia|ressurr|salvação|graça|evangelho",
    re.I,
)


def strip_accents(s: str) -> str:
    return "".join(
        c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn"
    )


def norm_key(title: str) -> str:
    t = strip_accents(title.lower().strip())
    t = re.sub(r"^doutrina\s+(da|de|do|das|dos)\s+", "", t)
    t = re.sub(r"[^a-z0-9]+", " ", t).strip()
    return t


def normalize_raw_kb(text: str) -> str:
    """Normaliza KB legados com \\r\\n literal e BOM; repara mojibake só quando detectado."""
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


def read_disc_file(code: str, name: str, filename: str) -> str | None:
    for folder in BASE.iterdir():
        if folder.is_dir() and folder.name.startswith(f"{code} "):
            p = folder / filename
            if p.exists():
                return normalize_raw_kb(
                    p.read_text(encoding="utf-8", errors="replace")
                )
    return None


def parse_h3_blocks(text: str) -> list[tuple[str, str]]:
    blocks: list[tuple[str, str]] = []
    parts = re.split(r"\n(?=### )", text)
    for part in parts:
        part = part.strip()
        if not part.startswith("### "):
            continue
        lines = part.split("\n", 1)
        title = lines[0].replace("### ", "").strip()
        body = lines[1].strip() if len(lines) > 1 else ""
        if title and not title.startswith("#"):
            blocks.append((title, body))
    return blocks


def normalize_section_name(name: str) -> str:
    n = strip_accents(name.upper().strip())
    n = re.sub(r"[^A-Z0-9 ]+", " ", n)
    n = " ".join(n.split())
    if "VIS" in n and "GERAL" in n:
        return "VISÃO GERAL"
    if "FUNDAMENTACAO" in n and "BIBLICA" in n:
        return "FUNDAMENTAÇÃO BÍBLICA"
    if "HERESIAS" in n and "RELACIONADAS" in n:
        return "HERESIAS RELACIONADAS"
    if "APLICACOES" in n:
        return "APLICAÇÕES"
    if "PALAVRAS" in n and "CHAVE" in n:
        return "PALAVRAS-CHAVE"
    aliases = {
        "VISAO GERAL": "VISÃO GERAL",
        "CONHECIMENTO FUNDAMENTAL": "CONHECIMENTO FUNDAMENTAL",
        "FUNDAMENTACAO BIBLICA": "FUNDAMENTAÇÃO BÍBLICA",
        "HERESIAS OU DISTORCOES RELACIONADAS": "HERESIAS RELACIONADAS",
        "APLICACOES PRATICAS": "APLICAÇÕES",
        "RELACIONAMENTOS": "RELACIONAMENTOS",
        "CONTROVERSIAS": "CONTROVÉRSIAS",
    }
    return aliases.get(n, name.upper().strip())


def parse_kb_h1_sections(text: str) -> dict[str, str]:
    sections: dict[str, str] = {}
    current = None
    buf: list[str] = []
    for line in text.splitlines():
        if line.startswith("# "):
            head = line[2:].strip()
            if not head or head.upper().startswith("KB_MASTER"):
                continue
            if current:
                sections[current] = "\n".join(buf).strip()
            current = normalize_section_name(head)
            buf = []
        elif current is not None:
            buf.append(line)
    if current:
        sections[current] = "\n".join(buf).strip()
    return sections


def parse_bullet_entries(section: str) -> list[tuple[str, str]]:
    entries: list[tuple[str, str]] = []
    for line in section.splitlines():
        m = re.match(r"^-\s+\*\*(.+?)\*\*:\s*(.+)$", line.strip())
        if m:
            entries.append((m.group(1).strip(), m.group(2).strip()))
        m2 = re.match(r"^-\s+\*\*(.+?)\*\*\s*<[^>]+>\s*\*\*(.+?)\*\*:\s*(.+)$", line.strip())
        if m2:
            entries.append((m2.group(1).strip(), f"{m2.group(2)}: {m2.group(3)}"))
    return entries


def extract_list_items(section: str, patterns: list[str]) -> list[str]:
    items: list[str] = []
    for pat in patterns:
        for m in re.finditer(pat, section, re.M | re.I):
            items.append(m.group(1).strip())
    for line in section.splitlines():
        m = re.match(r"^\d+\.\s+\*\*(.+?)\*\*", line)
        if m:
            items.append(m.group(1).strip())
        m = re.match(r"^-\s+\*\*(.+?)\*\*", line)
        if m:
            items.append(m.group(1).strip())
    return items


def merge_entry(store: dict, key: str, title: str, body: str, source: str) -> None:
    if key not in store:
        store[key] = {"title": title, "body": body, "sources": [source]}
        return
    e = store[key]
    if source not in e["sources"]:
        e["sources"].append(source)
    if len(body) > len(e["body"]):
        e["body"] = body
        e["title"] = title


def format_sources(sources: list[str]) -> str:
    return "; ".join(sources)


def format_entry(title: str, body: str, sources: list[str], extra: str = "") -> str:
    src = f"\n- **Fontes**: {format_sources(sources)}"
    cross = f"\n{extra}" if extra else ""
    return f"### {title}\n{body}{src}{cross}\n"


def main() -> None:
    visao_parts: list[str] = []
    conceitos: dict[str, dict] = {}
    doutrinas: dict[str, dict] = {}
    personagens: dict[str, dict] = {}
    eventos: dict[str, dict] = {}
    versiculos: dict[str, dict] = {}
    hermeneutica: dict[str, dict] = {}
    apologetica: dict[str, dict] = {}
    geografia: dict[str, dict] = {}
    cristologia: dict[str, dict] = {}
    relacionamentos: list[str] = []
    palavras_chave: set[str] = set()
    indice_temas: list[str] = []

    for code, dname in DISCIPLINES:
        source = f"{code} {dname}"
        kb = read_disc_file(code, dname, "KB_MASTER.md")
        dout = read_disc_file(code, dname, "DOUTRINAS.md")
        dic = read_disc_file(code, dname, "DICIONARIO.md")
        ver = read_disc_file(code, dname, "VERSICULOS.md")
        ind = read_disc_file(code, dname, "INDICE_SEMANTICO.md")

        if kb:
            secs = parse_kb_h1_sections(kb)
            vis = secs.get("VISÃO GERAL", "")
            if vis:
                tema = re.search(r"## Tema Principal\s*\n+(.+?)(?=\n## |\Z)", vis, re.S)
                resumo = re.search(
                    r"## Resumo Executivo\s*\n+(.+?)(?=\n---|\n# |\Z)", vis, re.S
                )
                obj = re.search(
                    r"## Objetivos[^\n]*\s*\n+(.+?)(?=\n## |\n---|\Z)", vis, re.S
                )
                block = [f"#### {source}"]
                if tema:
                    block.append(f"- **Tema**: {tema.group(1).strip()}")
                if obj:
                    obj_text = obj.group(1).strip()
                    if len(obj_text) > 800:
                        obj_text = obj_text[:800] + "..."
                    block.append(f"- **Objetivos**:\n{obj_text}")
                if resumo:
                    block.append(resumo.group(1).strip())
                if len(block) > 1:
                    visao_parts.append("\n".join(block))

            fund = secs.get("CONHECIMENTO FUNDAMENTAL", "")
            if fund:
                for item in extract_list_items(
                    fund,
                    [
                        r"^\d+\.\s+\*\*(.+?)\*\*",
                        r"^-\s+\*\*(.+?)\*\*:\s*(.+)$",
                    ],
                ):
                    k = norm_key(item)
                    merge_entry(conceitos, k, item, "", source)

                for title, body in parse_h3_blocks(fund):
                    k = norm_key(title)
                    merge_entry(conceitos, k, title, body, source)

            for title, body in parse_h3_blocks(secs.get("DOUTRINAS", "") + "\n" + fund):
                if "doutrina" in title.lower() or body:
                    k = norm_key(title)
                    merge_entry(doutrinas, k, title, body, source)

            pers_section = secs.get("CONHECIMENTO FUNDAMENTAL", "") + secs.get("PERSONAGENS", "")
            for item in extract_list_items(pers_section, [r"## Personagens[^\n]+\n+([\s\S]+?)(?=\n## |\Z)"]):
                pass
            if "## Personagens" in (secs.get("CONHECIMENTO FUNDAMENTAL", "") + kb):
                m = re.search(r"## Personagens[^\n]*\n+([\s\S]+?)(?=\n## |\n# |\Z)", kb)
                if m:
                    for line in m.group(1).splitlines():
                        pm = re.match(r"^-\s+\*\*(.+?)\*\*:\s*(.+)$", line.strip())
                        if pm:
                            k = norm_key(pm.group(1))
                            merge_entry(
                                personagens,
                                k,
                                pm.group(1),
                                pm.group(2).strip(),
                                source,
                            )

            if "## Eventos Históricos" in kb:
                m = re.search(r"## Eventos Históricos\n+([\s\S]+?)(?=\n---|\n# |\Z)", kb)
                if m:
                    for line in m.group(1).splitlines():
                        em = re.match(r"^\d+\.\s+\*\*(.+?)\*\*:\s*(.+)$", line.strip())
                        if em:
                            k = norm_key(em.group(1))
                            merge_entry(eventos, k, em.group(1), em.group(2).strip(), source)

            rel = secs.get("RELACIONAMENTOS", "")
            for line in rel.splitlines():
                line = line.strip()
                if line.startswith("- **"):
                    relacionamentos.append(f"- [{source}] {line[2:]}")

            her = secs.get("HERESIAS RELACIONADAS", "")
            for title, body in parse_h3_blocks(her + "\n" + secs.get("CONTROVÉRSIAS", "")):
                k = norm_key(title)
                merge_entry(apologetica, k, title, body, source)
            for title, body in parse_bullet_entries(her):
                k = norm_key(title)
                merge_entry(apologetica, k, title, body, source)
            for title, body in parse_bullet_entries(secs.get("CONTROVÉRSIAS", "")):
                k = norm_key(title)
                merge_entry(apologetica, k, title, body, source)

        if code in APOLOGETICS_IDS and dout:
            for title, body in parse_h3_blocks(dout):
                k = norm_key(title)
                merge_entry(apologetica, k, title, body, source)

            pk = secs.get("PALAVRAS-CHAVE", "")
            for token in re.split(r"[,;\n]+", pk):
                t = token.strip()
                if t and len(t) > 2:
                    palavras_chave.add(t)

        if dout:
            for title, body in parse_h3_blocks(dout):
                k = norm_key(title)
                merge_entry(doutrinas, k, title, body, source)
                if CHRISTOLOGY_KEYWORDS.search(title + body):
                    merge_entry(cristologia, k, title, body, source)

        if dic:
            for title, body in parse_h3_blocks(dic):
                tipo_m = re.search(r"-\s+\*\*Tipo\*\*:\s*(\w+)", body)
                tipo = tipo_m.group(1).lower() if tipo_m else "conceito"
                k = norm_key(title)
                if tipo == "personagem":
                    merge_entry(personagens, k, title, body, source)
                elif tipo == "evento":
                    merge_entry(eventos, k, title, body, source)
                elif tipo in ("heresia", "seita") or (
                    code in APOLOGETICS_IDS
                    and any(
                        w in title.lower()
                        for w in (
                            "seita",
                            "heresia",
                            "catolic",
                            "espirit",
                            "mormon",
                            "advent",
                            "jeová",
                            "nova era",
                            "maçon",
                            "islam",
                            "evoluc",
                            "unicidade",
                            "budismo",
                            "moon",
                        )
                    )
                ):
                    merge_entry(apologetica, k, title, body, source)
                elif tipo == "cidade" or "local" in tipo or "geografia" in body.lower():
                    merge_entry(geografia, k, title, body, source)
                else:
                    merge_entry(conceitos, k, title, body, source)
                if code in HERMENEUTICS_IDS or "hermenêut" in body.lower() or "exegese" in body.lower():
                    merge_entry(hermeneutica, k, title, body, source)
                if code in GEOGRAPHY_IDS:
                    merge_entry(geografia, k, title, body, source)
                if CHRISTOLOGY_KEYWORDS.search(title + body):
                    merge_entry(cristologia, k, title, body, source)

        if ver:
            for title, body in parse_h3_blocks(ver):
                k = norm_key(title)
                merge_entry(versiculos, k, title, body, source)

        if ind:
            for title, body in parse_h3_blocks(ind):
                indice_temas.append(
                    f"### {title}\n- **Disciplina âncora**: {source}\n{body}\n"
                )
                if code in HERMENEUTICS_IDS:
                    merge_entry(hermeneutica, norm_key(title), title, body, source)

    # Dedupe relacionamentos
    rel_seen: set[str] = set()
    rel_unique: list[str] = []
    for r in relacionamentos:
        rk = norm_key(r)
        if rk not in rel_seen:
            rel_seen.add(rk)
            rel_unique.append(r)

    lines: list[str] = [
        "---",
        'nivel: "Básico em Teologia"',
        "disciplinas_total: 12",
        "aulas_total: 187",
        "artefatos_fonte: 5",
        "versao: 1.0.0",
        "fase: 2",
        "---",
        "",
        "# KB_BASICO_COMPLETO — Curso Básico em Teologia",
        "",
        "Base de conhecimento unificada consolidada a partir dos artefatos `KB_MASTER.md`, "
        "`DOUTRINAS.md`, `DICIONARIO.md`, `VERSICULOS.md` e `INDICE_SEMANTICO.md` "
        "das doze disciplinas do Curso Básico. Entradas duplicadas foram fundidas por "
        "chave normalizada; a entrada mais completa foi preservada. Referências cruzadas "
        "apontam para disciplinas de origem.",
        "",
        "## Índice de Disciplinas Fonte",
        "",
    ]
    for code, dname in DISCIPLINES:
        lines.append(f"- **{code}** — {dname}")

    lines.extend(["", "# VISÃO GERAL", ""])
    lines.extend(visao_parts)

    lines.extend(["", "# CONCEITOS FUNDAMENTAIS", ""])
    for k in sorted(conceitos.keys()):
        e = conceitos[k]
        if e["body"]:
            lines.append(format_entry(e["title"], e["body"], e["sources"]))
        elif e["title"] and len(e["sources"]) > 0:
            lines.append(
                f"### {e['title']}\n- **Fontes**: {format_sources(e['sources'])}\n"
            )

    lines.extend(["", "# DOUTRINAS", ""])
    for k in sorted(doutrinas.keys()):
        e = doutrinas[k]
        lines.append(format_entry(e["title"], e["body"], e["sources"]))

    lines.extend(["", "# PERSONAGENS", ""])
    for k in sorted(personagens.keys()):
        e = personagens[k]
        lines.append(format_entry(e["title"], e["body"], e["sources"]))

    lines.extend(["", "# EVENTOS HISTÓRICOS", ""])
    for k in sorted(eventos.keys()):
        e = eventos[k]
        lines.append(format_entry(e["title"], e["body"], e["sources"]))

    lines.extend(["", "# FUNDAMENTAÇÃO BÍBLICA", ""])
    for k in sorted(versiculos.keys()):
        e = versiculos[k]
        lines.append(format_entry(e["title"], e["body"], e["sources"]))

    lines.extend(["", "# HERMENÊUTICA", ""])
    lines.append(
        "Consolidação temática das disciplinas **02 Métodos de Estudos Bíblicos**, "
        "**03 Homilética** e **10 Hermenêutica**, com entradas correlatas do dicionário.\n"
    )
    for k in sorted(hermeneutica.keys()):
        e = hermeneutica[k]
        lines.append(format_entry(e["title"], e["body"], e["sources"]))

    lines.extend(["", "# APOLOGÉTICA E HERESIAS", ""])
    lines.append(
        "Consolidação centrada na disciplina **12 Heresiologia**, integrada a heresias e "
        "controvérsias registradas nos `KB_MASTER.md` de todas as disciplinas.\n"
    )
    for k in sorted(apologetica.keys()):
        e = apologetica[k]
        lines.append(format_entry(e["title"], e["body"], e["sources"]))

    lines.extend(["", "# GEOGRAFIA BÍBLICA", ""])
    lines.append(
        "Consolidação das disciplinas **04 Arqueologia e Geografia 1** e "
        "**05 Arqueologia e Geografia 2**, com locais e conceitos geográficos correlatos.\n"
    )
    for k in sorted(geografia.keys()):
        e = geografia[k]
        lines.append(format_entry(e["title"], e["body"], e["sources"]))

    lines.extend(["", "# CRISTOLOGIA", ""])
    lines.append(
        "Entradas doutrinárias e lexicais relacionadas a Cristo, Messias, Verbo, encarnação, "
        "obra redentora e evangelhos (disciplinas 01, 08, 11 e correlatas).\n"
    )
    for k in sorted(cristologia.keys()):
        e = cristologia[k]
        lines.append(format_entry(e["title"], e["body"], e["sources"]))

    lines.extend(["", "# PALAVRAS-CHAVE GLOBAIS", ""])
    lines.append(", ".join(sorted(palavras_chave, key=lambda x: strip_accents(x).lower())))

    lines.extend(["", "# RELACIONAMENTOS GLOBAIS", ""])
    lines.extend(["## Triplas e conexões (KB_MASTER)", ""])
    lines.extend(rel_unique[:500])
    lines.extend(["", "## Temas semânticos (INDICE_SEMANTICO)", ""])
    lines.extend(indice_temas)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    content = "\n".join(lines)
    OUT_FILE.write_text(content, encoding="utf-8")
    print(f"Written: {OUT_FILE}")
    print(f"Lines: {len(lines)}")
    print(
        f"Counts: conceitos={len(conceitos)} doutrinas={len(doutrinas)} "
        f"personagens={len(personagens)} eventos={len(eventos)} "
        f"versiculos={len(versiculos)} herm={len(hermeneutica)} "
        f"apolo={len(apologetica)} geo={len(geografia)} cristo={len(cristologia)}"
    )


if __name__ == "__main__":
    main()
