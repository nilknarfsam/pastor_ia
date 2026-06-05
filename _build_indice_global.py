#!/usr/bin/env python3
"""Gera INDICE_GLOBAL.md — navegação temática global do Curso Básico."""
from __future__ import annotations

import re
import unicodedata
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BASE = ROOT / "01 Básico em Teologia"
OUT_DIR = ROOT / "90_Knowledge_Base"
KB_FILE = OUT_DIR / "KB_BASICO_COMPLETO.md"
DIC_FILE = OUT_DIR / "DICIONARIO_GLOBAL.md"
OUT_FILE = OUT_DIR / "INDICE_GLOBAL.md"

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

SECTIONS = [
    "TEOLOGIA",
    "BIBLIOLOGIA",
    "CRISTOLOGIA",
    "PNEUMATOLOGIA",
    "SOTERIOLOGIA",
    "ECLESIOLOGIA",
    "ESCATOLOGIA",
    "HERMENÊUTICA",
    "HOMILÉTICA",
    "APOLOGÉTICA",
    "HERESIAS",
    "GEOGRAFIA BÍBLICA",
    "PERSONAGENS",
    "EVENTOS HISTÓRICOS",
    "LIVROS BÍBLICOS",
]

SECTION_INTRO = {
    "TEOLOGIA": "Fundamentos da ciência teológica, teontologia, antropologia e doutrinas gerais sobre Deus e o homem.",
    "BIBLIOLOGIA": "Inspiração, autoridade, canonização e integridade das Escrituras.",
    "CRISTOLOGIA": "Pessoa, naturezas, obra e ofícios de Jesus Cristo nos Evangelhos e epístolas.",
    "PNEUMATOLOGIA": "Espírito Santo, sua obra na criação, encarnação, igreja e vida do crente.",
    "SOTERIOLOGIA": "Salvação, graça, justificação, regeneração, santificação e expiação.",
    "ECLESIOLOGIA": "Igreja, ministério, sacramentos e missão no mundo.",
    "ESCATOLOGIA": "Juízo, ressurreição, vida eterna, Apocalipse e consumação das eras.",
    "HERMENÊUTICA": "Princípios de interpretação bíblica, exegese e aplicação da Palavra.",
    "HOMILÉTICA": "Arte da pregação, estrutura do sermão e comunicação pastoral.",
    "APOLOGÉTICA": "Defesa da fé, refutação de objeções e discernimento doutrinário.",
    "HERESIAS": "Movimentos seitas, distorções doutrinárias e respostas bíblicas.",
    "GEOGRAFIA BÍBLICA": "Lugares, arqueologia, geografia e contexto territorial do mundo bíblico.",
    "PERSONAGENS": "Figuras bíblicas, teólogos e personagens históricos catalogados no curso.",
    "EVENTOS HISTÓRICOS": "Acontecimentos bíblicos e históricos relevantes à formação teológica.",
    "LIVROS BÍBLICOS": "Livros canônicos estudados e referenciados nas disciplinas.",
}

DISCIPLINE_SECTIONS: dict[str, list[str]] = {
    "01": ["TEOLOGIA", "BIBLIOLOGIA", "CRISTOLOGIA"],
    "02": ["BIBLIOLOGIA", "HERMENÊUTICA"],
    "03": ["HOMILÉTICA", "HERMENÊUTICA"],
    "04": ["GEOGRAFIA BÍBLICA"],
    "05": ["GEOGRAFIA BÍBLICA"],
    "06": ["BIBLIOLOGIA", "TEOLOGIA", "LIVROS BÍBLICOS"],
    "07": ["TEOLOGIA", "SOTERIOLOGIA", "ESCATOLOGIA"],
    "08": ["CRISTOLOGIA", "SOTERIOLOGIA", "ECLESIOLOGIA", "ESCATOLOGIA", "PNEUMATOLOGIA"],
    "09": ["TEOLOGIA", "LIVROS BÍBLICOS", "HERMENÊUTICA"],
    "10": ["HERMENÊUTICA", "BIBLIOLOGIA"],
    "11": ["CRISTOLOGIA", "SOTERIOLOGIA", "LIVROS BÍBLICOS"],
    "12": ["HERESIAS", "APOLOGÉTICA"],
}

KB_DIRECT: dict[str, list[str]] = {
    "HERMENÊUTICA": ["HERMENÊUTICA"],
    "GEOGRAFIA BÍBLICA": ["GEOGRAFIA BÍBLICA"],
    "CRISTOLOGIA": ["CRISTOLOGIA"],
    "PERSONAGENS": ["PERSONAGENS"],
    "EVENTOS HISTÓRICOS": ["EVENTOS HISTÓRICOS"],
}

SECTION_PATTERNS: dict[str, list[str]] = {
    "TEOLOGIA": [
        r"teologi", r"teontolog", r"\bdeus\b", r"trindade", r"atributo", r"revela",
        r"antropolog", r"hamartolog", r"dispensa", r"provid", r"decretos", r"imutabil",
        r"omnipot", r"omnisci", r"unicidade", r"criação", r"queda", r"pecado original",
        r"teologia natural", r"teologia revelada", r"angelolog", r"anjo",
    ],
    "BIBLIOLOGIA": [
        r"bibliolog", r"inspira", r"autógrafo", r"inerr", r"canon", r"canônic",
        r"manuscrito", r"vulgata", r"septuaginta", r"theopneustos", r"\bbíblia\b",
        r"sola scriptura", r"texto bíblico", r"verbal", r"copista", r"autógraf",
    ],
    "CRISTOLOGIA": [
        r"cristolog", r"cristo", r"messias", r"encarna", r"kenosis", r"verbo",
        r"euangelion", r"evangelho", r"expia", r"reden", r"ressurr.*cristo",
        r"filho de deus", r"filho do homem", r"ofício.*cristo", r"preexist",
    ],
    "PNEUMATOLOGIA": [
        r"pneumatolog", r"espírito santo", r"espirito santo", r"paráclito",
        r"consolador", r"batismo.*espírito", r"iluminação", r"unção",
    ],
    "SOTERIOLOGIA": [
        r"soteriolog", r"salva", r"graça", r"justifica", r"regenera", r"santifica",
        r"\bfé\b", r"arrepend", r"propicia", r"expia", r"reden", r"conversão",
        r"reconcilia", r"mediador",
    ],
    "ECLESIOLOGIA": [
        r"eclesiolog", r"\bigreja\b", r"ministério", r"diácono", r"presbítero",
        r"ceia", r"batismo", r"comissão", r"corpo de cristo", r"pedra angular",
    ],
    "ESCATOLOGIA": [
        r"escatolog", r"apocalipse", r"parousia", r"arrebat", r"milênio", r"juízo",
        r"vida eterna", r"purgat", r"ressurr", r"segunda vinda", r"reino eterno",
    ],
    "HERMENÊUTICA": [
        r"hermenêut", r"hermeneut", r"exegese", r"eisegese", r"interpreta",
        r"contexto", r"gênero literário", r"abismo", r"iluminação", r"aplicar",
        r"intenção autoral", r"axioma",
    ],
    "HOMILÉTICA": [
        r"homilét", r"homilet", r"prega", r"sermão", r"exordium", r"peroração",
        r"contato visual", r"postura", r"adequação linguística", r"desenvolvimento",
    ],
    "APOLOGÉTICA": [
        r"apologét", r"apolog", r"defesa da fé", r"provas da existência",
        r"refuta", r"discernimento", r"haireses",
    ],
    "HERESIAS": [
        r"heresia", r"seita", r"arianismo", r"gnosticismo", r"mormon", r"adventismo",
        r"espiritismo", r"catolicismo romano", r"testemunhas de jeová", r"nova era",
        r"islamismo", r"budismo", r"maçonaria", r"evolucionismo", r"pelagianismo",
        r"docetismo", r"marcionismo", r"transubstanciação", r"purgatório",
    ],
    "GEOGRAFIA BÍBLICA": [
        r"geograf", r"arqueolog", r"\bcidade\b", r"\blugar\b", r"monte\b", r"vale\b",
        r"rio\b", r"mar\b", r"jerusalém", r"israel", r"canan", r"palestin",
        r"oriente médio", r"mapa", r"escavação",
    ],
}

HERESY_MARKERS = re.compile(
    r"heresia|seita|arianismo|gnosticismo|mormon|adventismo|espiritismo|"
    r"catolicismo|testemunhas|nova era|islamismo|budismo|maçonaria|"
    r"evolucionismo|pelagianismo|docetismo|marcionismo|transubstanciação|"
    r"purgatório|moonismo|teosofismo|kardec",
    re.I,
)

DOUTRINA_MARKERS = re.compile(r"^doutrina\b|doutrina da|doutrina de|doutrina do", re.I)
EVENTO_MARKERS = re.compile(
    r"concílio|queda|exílio|conquista|reforma|perseguição|batismo de|"
    r"grande comissão|pentecostes|passagem|libertação|destruição",
    re.I,
)

VERSE_REF = re.compile(
    r"\d+:\d+|\d+:\d+-\d+|\b(?:Gn|Mt|Mc|Lc|Jo|At|Rm|Sl|Pv|Ec|Is|Jr|Ez|Dn)\b",
    re.I,
)
BIBLE_BOOKS = re.compile(
    r"^(Gênesis|Êxodo|Levítico|Números|Deuteronômio|Josué|Juízes|Rute|"
    r"Samuel|Reis|Crônicas|Esdras|Neemias|Ester|Jó|Salmos|Provérbios|"
    r"Eclesiastes|Cânticos|Isaías|Jeremias|Lamentações|Ezequiel|Daniel|"
    r"Oseias|Joel|Amós|Obadias|Jonas|Miqueias|Naum|Habacuque|Sofonias|"
    r"Ageu|Zacarias|Malaquias|Mateus|Marcos|Lucas|João|Atos|Romanos|"
    r"Coríntios|Gálatas|Efésios|Filipenses|Colossenses|Tessalonicenses|"
    r"Timóteo|Tito|Filemom|Hebreus|Tiago|Pedro|Judas|Apocalipse)\b",
    re.I,
)
KB_THEMATIC_SECTIONS = {
    "HERMENÊUTICA",
    "APOLOGÉTICA E HERESIAS",
    "GEOGRAFIA BÍBLICA",
    "CRISTOLOGIA",
    "PERSONAGENS",
    "EVENTOS HISTÓRICOS",
}
NOISE_TERMS = re.compile(
    r"^(não identificad|não aplicável|geral|—|-|\.\.\.)",
    re.I,
)


@dataclass
class SectionData:
    conceitos: set[str] = field(default_factory=set)
    doutrinas: set[str] = field(default_factory=set)
    personagens: set[str] = field(default_factory=set)
    eventos: set[str] = field(default_factory=set)
    disciplinas: set[str] = field(default_factory=set)


def strip_accents(s: str) -> str:
    return "".join(
        c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn"
    )


def norm_key(s: str) -> str:
    t = strip_accents(s.lower().strip())
    return re.sub(r"[^a-z0-9]+", " ", t).strip()


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


def split_items(value: str) -> list[str]:
    if not value or value.strip() in ("—", "-", "Não identificado", "Não aplicável"):
        return []
    return [p.strip() for p in re.split(r"[,;]\s*", value) if p.strip() and len(p.strip()) > 1]


def parse_field(body: str, field_name: str) -> str:
    m = re.search(rf"-\s+\*\*{re.escape(field_name)}\*\*:\s*(.+)", body)
    return m.group(1).strip() if m else ""


def parse_h3_blocks(text: str, stop_at: str | None = None) -> list[tuple[str, str]]:
    if stop_at and stop_at in text:
        text = text.split(stop_at)[0]
    blocks: list[tuple[str, str]] = []
    for part in re.split(r"\n(?=### )", text):
        part = part.strip()
        if not part.startswith("### "):
            continue
        lines = part.split("\n", 1)
        title = lines[0].replace("### ", "").strip()
        body = lines[1].strip() if len(lines) > 1 else ""
        if title:
            blocks.append((title, body))
    return blocks


def clean_term(name: str) -> str:
    s = name.strip().strip(".")
    s = re.sub(r"\s+", " ", s)
    return s


def is_verse_or_noise(name: str) -> bool:
    s = clean_term(name)
    if not s or len(s) < 2:
        return True
    if NOISE_TERMS.search(s):
        return True
    if VERSE_REF.search(s):
        return True
    if BIBLE_BOOKS.match(s) and re.search(r"\d", s):
        return True
    if re.match(r"^\d+[\./\d]*$", s):
        return True
    if re.match(r"^[A-Za-zÀ-ÿ]+\s+\d+$", s) and BIBLE_BOOKS.match(s.split()[0]):
        return True
    if s.endswith(")") and "(" not in s:
        return True
    if "Ã" in s or "â€™" in s:
        return True
    return False


def score_sections(blob_norm: str) -> dict[str, int]:
    scores: dict[str, int] = {}
    for sec, patterns in SECTION_PATTERNS.items():
        if sec in ("PERSONAGENS", "EVENTOS HISTÓRICOS", "LIVROS BÍBLICOS"):
            continue
        n = sum(1 for p in patterns if re.search(p, blob_norm))
        if n:
            scores[sec] = n
    return scores


def category_sections(categoria: str | None) -> set[str]:
    found: set[str] = set()
    if categoria == "Livro Bíblico":
        found.add("LIVROS BÍBLICOS")
    elif categoria in ("Heresia", "Seita"):
        found.add("HERESIAS")
    elif categoria == "Pessoa":
        found.add("PERSONAGENS")
    elif categoria == "Evento":
        found.add("EVENTOS HISTÓRICOS")
    elif categoria == "Lugar":
        found.add("GEOGRAFIA BÍBLICA")
    return found


def classify_sections(
    title: str,
    text: str = "",
    *,
    categoria: str | None = None,
    kb_section: str | None = None,
    discipline: str | None = None,
    use_discipline_defaults: bool = True,
    mode: str = "all",
) -> set[str]:
    blob = f"{title} {text}"
    blob_norm = strip_accents(blob.lower())
    found: set[str] = set()

    if kb_section in KB_DIRECT:
        return set(KB_DIRECT[kb_section])

    if kb_section == "APOLOGÉTICA E HERESIAS":
        return {"HERESIAS"} if HERESY_MARKERS.search(blob) else {"APOLOGÉTICA"}

    found.update(category_sections(categoria))

    scores = score_sections(blob_norm)
    if mode == "primary":
        if scores:
            best = max(scores, key=scores.get)
            found.add(best)
        elif categoria == "Doutrina" or DOUTRINA_MARKERS.search(title):
            found.add("TEOLOGIA")
        elif not found:
            found.add(primary_section(categoria))
    else:
        found.update(scores.keys())
        if use_discipline_defaults and discipline and discipline in DISCIPLINE_SECTIONS:
            found.update(DISCIPLINE_SECTIONS[discipline])
        if DOUTRINA_MARKERS.search(title):
            found.add("TEOLOGIA")
        if not found:
            found.add(primary_section(categoria))

    return found


def primary_section(categoria: str | None) -> str:
    return {
        "Pessoa": "PERSONAGENS",
        "Evento": "EVENTOS HISTÓRICOS",
        "Lugar": "GEOGRAFIA BÍBLICA",
        "Livro Bíblico": "LIVROS BÍBLICOS",
        "Heresia": "HERESIAS",
        "Seita": "HERESIAS",
        "Doutrina": "TEOLOGIA",
        "Instituição": "TEOLOGIA",
    }.get(categoria or "", "TEOLOGIA")


def item_kind(name: str, categoria: str | None = None) -> str:
    if categoria == "Pessoa":
        return "personagens"
    if categoria == "Evento":
        return "eventos"
    if categoria in ("Doutrina",) or DOUTRINA_MARKERS.search(name):
        return "doutrinas"
    if categoria == "Livro Bíblico":
        return "conceitos"
    if EVENTO_MARKERS.search(name):
        return "eventos"
    return "conceitos"


def add_item(
    store: dict[str, SectionData],
    sections: set[str],
    name: str,
    kind: str,
    disciplina: str | None = None,
) -> None:
    name = clean_term(name)
    if is_verse_or_noise(name):
        return
    for sec in sections:
        if sec not in store:
            continue
        bucket = getattr(store[sec], kind)
        bucket.add(name)
        if disciplina:
            store[sec].disciplinas.add(disciplina)


def parse_dic_global(store: dict[str, SectionData]) -> int:
    text = normalize_raw(DIC_FILE.read_text(encoding="utf-8", errors="replace"))
    count = 0
    for title, body in parse_h3_blocks(text, stop_at="## Estatísticas"):
        count += 1
        cat = parse_field(body, "Categoria")
        disc_raw = parse_field(body, "Disciplinas Relacionadas")
        disciplinas = split_items(disc_raw.replace(";", ","))
        def_blob = parse_field(body, "Definição Consolidada")
        sections = classify_sections(
            title, def_blob, categoria=cat, use_discipline_defaults=False, mode="primary"
        )

        kind = item_kind(title, cat)
        for sec in sections:
            add_item(store, {sec}, title, kind)
            for d in disciplinas:
                store[sec].disciplinas.add(d)

        for t in split_items(parse_field(body, "Termos Relacionados").replace(";", ",")):
            if is_verse_or_noise(t):
                continue
            t_kind = item_kind(t)
            t_sections = classify_sections(
                t, use_discipline_defaults=False, mode="primary"
            ) & sections
            if not t_sections:
                t_sections = sections
            for sec in t_sections:
                add_item(store, {sec}, t, t_kind)

    return count


def parse_indice_semantico(store: dict[str, SectionData]) -> int:
    count = 0
    for code, dname in DISCIPLINES:
        disc_label = f"{code} {dname}"
        for folder in BASE.iterdir():
            if not folder.is_dir() or not folder.name.startswith(f"{code} "):
                continue
            path = folder / "INDICE_SEMANTICO.md"
            if not path.exists():
                continue
            text = normalize_raw(path.read_text(encoding="utf-8", errors="replace"))
            for tema, body in parse_h3_blocks(text):
                count += 1
                fields = {
                    "conceitos": parse_field(body, "Conceitos relacionados"),
                    "doutrinas": parse_field(body, "Doutrinas relacionadas"),
                    "personagens": parse_field(body, "Personagens relacionados"),
                }
                blob = " ".join(fields.values())
                tema_secs = classify_sections(
                    tema, blob, discipline=code, use_discipline_defaults=True, mode="primary"
                )
                add_item(store, tema_secs, tema, "conceitos", disc_label)

                for item in split_items(fields["conceitos"]):
                    secs = classify_sections(
                        item, use_discipline_defaults=False, mode="primary"
                    )
                    add_item(store, secs, item, "conceitos", disc_label)
                    if EVENTO_MARKERS.search(item):
                        add_item(store, secs, item, "eventos", disc_label)
                for item in split_items(fields["doutrinas"]):
                    secs = classify_sections(
                        item, use_discipline_defaults=False, mode="primary"
                    )
                    add_item(store, secs, item, "doutrinas", disc_label)
                for item in split_items(fields["personagens"]):
                    secs = classify_sections(
                        item, categoria="Pessoa", use_discipline_defaults=False, mode="primary"
                    )
                    add_item(store, secs, item, "personagens", disc_label)
    return count


def parse_kb_basico(store: dict[str, SectionData]) -> int:
    text = normalize_raw(KB_FILE.read_text(encoding="utf-8", errors="replace"))
    count = 0
    current_section: str | None = None
    buf_title: str | None = None
    buf_lines: list[str] = []

    def flush() -> None:
        nonlocal count
        if not buf_title or not current_section:
            return
        body = "\n".join(buf_lines)
        fontes = parse_field(body, "Fontes")
        disciplinas = split_items(fontes.replace(";", ",")) if fontes else []
        sections = classify_sections(
            buf_title,
            body,
            kb_section=current_section,
            use_discipline_defaults=False,
        )
        if not sections:
            return
        count += 1
        kind = item_kind(buf_title)
        for sec in sections:
            add_item(store, {sec}, buf_title, kind)
            for d in disciplinas:
                store[sec].disciplinas.add(d)

    for line in text.splitlines():
        if line.startswith("# ") and not line.startswith("## "):
            flush()
            buf_title = None
            buf_lines = []
            head = line[2:].strip().upper()
            if head.startswith("KB_BASICO") or head not in KB_THEMATIC_SECTIONS:
                current_section = None
            else:
                current_section = head
            continue
        if line.startswith("### "):
            flush()
            buf_title = line[4:].strip()
            buf_lines = []
            continue
        if buf_title is not None:
            buf_lines.append(line)

    flush()
    return count


def sort_key(s: str) -> str:
    return strip_accents(s).lower()


def dedupe_sorted(items: set[str]) -> list[str]:
    seen: dict[str, str] = {}
    for item in items:
        k = norm_key(item)
        if k not in seen or len(item) > len(seen[k]):
            seen[k] = item
    return sorted(seen.values(), key=sort_key)


def format_section(sec: str, data: SectionData) -> list[str]:
    lines = [
        "",
        f"# {sec}",
        "",
        SECTION_INTRO.get(sec, ""),
        "",
        "## Conceitos Relacionados",
        "",
    ]
    raw_conceitos = data.conceitos - data.doutrinas - data.personagens - data.eventos
    if sec in ("PERSONAGENS", "EVENTOS HISTÓRICOS", "LIVROS BÍBLICOS"):
        raw_conceitos = {c for c in raw_conceitos if not re.match(r"^\d", c)}
    conceitos = dedupe_sorted(raw_conceitos)
    if conceitos:
        lines.extend(f"- {c}" for c in conceitos)
    else:
        lines.append("- —")

    lines.extend(["", "## Doutrinas Relacionadas", ""])
    doutrinas = dedupe_sorted(data.doutrinas)
    lines.extend(f"- {d}" for d in doutrinas) if doutrinas else lines.append("- —")

    lines.extend(["", "## Personagens Relacionados", ""])
    personagens = dedupe_sorted(data.personagens)
    lines.extend(f"- {p}" for p in personagens) if personagens else lines.append("- —")

    lines.extend(["", "## Eventos Relacionados", ""])
    eventos = dedupe_sorted(data.eventos)
    lines.extend(f"- {e}" for e in eventos) if eventos else lines.append("- —")

    lines.extend(["", "## Disciplinas Relacionadas", ""])
    disc_order = {f"{c} {n}": i for i, (c, n) in enumerate(DISCIPLINES)}
    disciplinas = sorted(data.disciplinas, key=lambda d: disc_order.get(d, 99))
    if disciplinas:
        lines.extend(f"- **{d.split(' ', 1)[0]}** — {d.split(' ', 1)[1]}" for d in disciplinas if " " in d)
    else:
        lines.append("- —")

    return lines


def main() -> None:
    store: dict[str, SectionData] = {s: SectionData() for s in SECTIONS}

    n_dic = parse_dic_global(store)
    n_ind = parse_indice_semantico(store)
    n_kb = parse_kb_basico(store)

    lines: list[str] = [
        "---",
        'nivel: "Básico em Teologia"',
        "disciplinas_total: 12",
        f"secoes_tematicas: {len(SECTIONS)}",
        "versao: 1.0.0",
        "fase: 2",
        "---",
        "",
        "# ÍNDICE GLOBAL — Pastor IA",
        "",
        "Navegação temática global do Curso Básico em Teologia, consolidada a partir de "
        "`KB_BASICO_COMPLETO.md`, `DICIONARIO_GLOBAL.md` e `INDICE_SEMANTICO.md` "
        "das doze disciplinas. Destinado à navegação principal da futura plataforma web.",
        "",
        "## Mapa de Seções",
        "",
    ]
    for sec in SECTIONS:
        lines.append(f"- [{sec}](#{sec.lower().replace(' ', '-').replace('í', 'i').replace('é', 'e').replace('ô', 'o').replace('á', 'a').replace('ê', 'e')})")

    stats_conceitos: Counter[str] = Counter()
    stats_total: Counter[str] = Counter()

    for sec in SECTIONS:
        data = store[sec]
        lines.extend(format_section(sec, data))
        n = (
            len(data.conceitos)
            + len(data.doutrinas)
            + len(data.personagens)
            + len(data.eventos)
        )
        stats_total[sec] = n
        stats_conceitos[sec] = len(data.conceitos)

    lines.extend(["", "---", "", "## Estatísticas", ""])
    lines.append(f"- **Fontes processadas**: DICIONARIO_GLOBAL ({n_dic} entradas), INDICE_SEMANTICO ({n_ind} temas), KB_BASICO_COMPLETO ({n_kb} entradas)")
    lines.append("")
    lines.append("### Itens por seção temática")
    lines.append("")
    for sec, n in stats_total.most_common():
        d = store[sec]
        lines.append(
            f"- **{sec}**: {n} itens "
            f"(conceitos {len(d.conceitos)}, doutrinas {len(d.doutrinas)}, "
            f"personagens {len(d.personagens)}, eventos {len(d.eventos)}, "
            f"disciplinas {len(d.disciplinas)})"
        )

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    OUT_FILE.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Written: {OUT_FILE}")
    print(f"Sources: dic={n_dic} ind={n_ind} kb={n_kb}")
    print("Top sections:", stats_total.most_common(5))


if __name__ == "__main__":
    main()
