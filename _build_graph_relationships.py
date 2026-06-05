#!/usr/bin/env python3
"""Gera GRAPH_RELATIONSHIPS.md — grafo semântico global do Curso Básico."""
from __future__ import annotations

import re
import unicodedata
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BASE = ROOT / "01 Básico em Teologia"
OUT_DIR = ROOT / "90_Knowledge_Base"
KB_FILE = OUT_DIR / "KB_BASICO_COMPLETO.md"
DIC_FILE = OUT_DIR / "DICIONARIO_GLOBAL.md"
INDICE_FILE = OUT_DIR / "INDICE_GLOBAL.md"
OUT_FILE = OUT_DIR / "GRAPH_RELATIONSHIPS.md"

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

ALLOWED_RELATIONS = {
    "ensina",
    "menciona",
    "conecta",
    "contradiz",
    "deriva de",
    "ocorre em",
    "associado a",
    "relacionado a",
    "fundamentado em",
    "explicado por",
}

CATEGORY_PRIORITY = {
    "Pessoa": 10,
    "Lugar": 9,
    "Evento": 8,
    "Livro Bíblico": 7,
    "Heresia": 7,
    "Seita": 7,
    "Doutrina": 6,
    "Instituição": 6,
    "Período Histórico": 5,
    "Conceito": 1,
}

CATEGORY_MAP = {
    "Pessoa": "Pessoa",
    "Lugar": "Lugar",
    "Doutrina": "Doutrina",
    "Conceito": "Conceito",
    "Evento": "Evento",
    "Livro Bíblico": "Livro Bíblico",
    "Heresia": "Heresia",
    "Seita": "Seita",
    "Instituição": "Instituição",
    "Período Histórico": "Período Histórico",
    "Termo Grego": "Conceito",
    "Termo Hebraico": "Conceito",
}

CANONICAL_ALIASES: dict[str, str] = {
    "guinoticismo": "Gnosticismo",
    "gnosticismo": "Gnosticismo",
    "instituto teologico renacer": "Instituto Teológico Renacer",
    "instituto teologico renace": "Instituto Teológico Renacer",
    "renacer instituto teologico": "Instituto Teológico Renacer",
    "pastor tiago dominguez": "Pastor Tiago Domínguez",
    "tiago dominguez": "Pastor Tiago Domínguez",
    "tiago domingus": "Pastor Tiago Domínguez",
    "pastor carvalho junior": "Pastor Carvalho Júnior",
    "carvalho junho": "Pastor Carvalho Júnior",
    "coelhada": "Goel",
    "vingador de sangue": "Goel",
    "aemia paputoliva": "Aelia Capitolina",
    "imeneutica": "Hermenêutica",
    "gensabele": "Jezabel",
    "atanasio": "Atanásio de Alexandria",
    "jesus": "Jesus Cristo",
    "cristo": "Jesus Cristo",
    "moises": "Moisés",
    "encarnacao": "Encarnação",
}

TAG_TO_RELATION: dict[str, str] = {
    "combate": "contradiz",
    "invalida": "contradiz",
    "opõe se a": "contradiz",
    "oposto a": "contradiz",
    "previne": "contradiz",
    "precede": "deriva de",
    "fonte para": "deriva de",
    "prepara": "deriva de",
    "parte_de": "deriva de",
    "vem de": "deriva de",
    "fundador_de": "deriva de",
    "inicia": "deriva de",
    "base_de": "deriva de",
    "fundamento_de": "fundamentado em",
    "implica": "fundamentado em",
    "marco_de": "ocorre em",
    "divide": "conecta",
    "modelo de": "ensina",
    "sistematiza": "explicado por",
    "apresenta": "relacionado a",
    "tema central de": "relacionado a",
    "espinha dorsal de": "associado a",
    "capacita": "associado a",
    "complementa": "associado a",
    "casamento com": "conecta",
    "exigem": "conecta",
    "método de": "explicado por",
    "produz": "deriva de",
    "gera": "deriva de",
    "legitimam": "fundamentado em",
    "orienta": "explicado por",
    "alinhada a": "fundamentado em",
    "unifica": "conecta",
    "autoridade_em": "associado a",
    "profeta_de": "associado a",
    "reivindica_papel_de": "relacionado a",
    "estrategia_de": "explicado por",
    "ferramenta_para": "explicado por",
    "exige": "explicado por",
}

VERSE_REF = re.compile(r"\d+:\d+|\d+:\d+-\d+", re.I)
NOISE = re.compile(r"^(não identificad|não aplicável|geral|—|-|\.\.\.)", re.I)


@dataclass(frozen=True)
class Edge:
    source: str
    relation: str
    target: str
    discipline: str
    fonte: str


def strip_accents(s: str) -> str:
    return "".join(
        c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn"
    )


def norm_key(s: str) -> str:
    t = strip_accents(s.lower().strip())
    return re.sub(r"[^a-z0-9]+", " ", t).strip()


def canonical(name: str) -> str:
    k = norm_key(name)
    return CANONICAL_ALIASES.get(k, name.strip())


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


def is_valid_entity(name: str) -> bool:
    s = name.strip().strip(".")
    if not s or len(s) < 2:
        return False
    if NOISE.search(s):
        return False
    if VERSE_REF.search(s) and len(s) < 30:
        return False
    if re.match(r"^\d+[\./\d]*$", s):
        return False
    if "Ã" in s:
        return False
    return True


def map_relation(tag: str) -> str:
    t = strip_accents(tag.lower().strip())
    return TAG_TO_RELATION.get(t, "relacionado a")


def split_items(value: str) -> list[str]:
    if not value:
        return []
    return [p.strip() for p in re.split(r"[,;]\s*", value) if p.strip()]


def parse_field(body: str, field: str) -> str:
    m = re.search(rf"-\s+\*\*{re.escape(field)}\*\*:\s*(.+)", body)
    return m.group(1).strip() if m else ""


class GraphBuilder:
    def __init__(self) -> None:
        self.nodes: dict[str, str] = {}
        self.edges: dict[tuple[str, str, str], Edge] = {}

    def set_category(self, name: str, cat: str) -> None:
        name = canonical(name)
        if not is_valid_entity(name):
            return
        mapped = CATEGORY_MAP.get(cat, "Conceito")
        cur = self.nodes.get(name)
        if cur is None or CATEGORY_PRIORITY.get(mapped, 0) > CATEGORY_PRIORITY.get(cur, 0):
            self.nodes[name] = mapped

    def infer_category(self, name: str) -> str:
        name = canonical(name)
        if name in self.nodes:
            return self.nodes[name]
        nk = norm_key(name)
        if nk in ("gnosticismo", "arianismo", "pelagianismo"):
            return "Heresia"
        if re.search(r"^doutrina\b", name, re.I):
            return "Doutrina"
        if re.search(
            r"^(gênesis|êxodo|levítico|mateus|marcos|lucas|joão|atos|romanos|salmos|pentateuco|evangelhos)\b",
            name,
            re.I,
        ):
            return "Livro Bíblico"
        if re.search(r"concílio|queda|reforma|pentecostes|exílio", name, re.I):
            return "Evento"
        if re.search(r"jerusalém|hebron|samaria|galileia|egito|canan", name, re.I):
            return "Lugar"
        return "Conceito"

    def add_edge(
        self,
        src: str,
        rel: str,
        tgt: str,
        discipline: str = "",
        fonte: str = "",
        src_cat: str | None = None,
        tgt_cat: str | None = None,
    ) -> None:
        src = canonical(src)
        tgt = canonical(tgt)
        if not is_valid_entity(src) or not is_valid_entity(tgt):
            return
        if norm_key(src) == norm_key(tgt):
            return
        rel = rel if rel in ALLOWED_RELATIONS else "relacionado a"
        if src_cat:
            self.set_category(src, src_cat)
        else:
            self.set_category(src, self.infer_category(src))
        if tgt_cat:
            self.set_category(tgt, tgt_cat)
        else:
            self.set_category(tgt, self.infer_category(tgt))
        key = (norm_key(src), rel, norm_key(tgt))
        edge = Edge(src, rel, tgt, discipline, fonte)
        if key not in self.edges or len(discipline) > len(self.edges[key].discipline):
            self.edges[key] = edge

    def preload_dic_categories(self) -> None:
        text = normalize_raw(DIC_FILE.read_text(encoding="utf-8", errors="replace"))
        for part in re.split(r"\n(?=### )", text.split("## Estatísticas")[0]):
            if not part.strip().startswith("### "):
                continue
            title = part.split("\n", 1)[0].replace("### ", "").strip()
            body = part.split("\n", 1)[1] if "\n" in part else ""
            cat = parse_field(body, "Categoria")
            self.set_category(title, cat)

    def parse_dic_global(self) -> int:
        text = normalize_raw(DIC_FILE.read_text(encoding="utf-8", errors="replace"))
        count = 0
        for part in re.split(r"\n(?=### )", text.split("## Estatísticas")[0]):
            if not part.strip().startswith("### "):
                continue
            lines = part.split("\n", 1)
            title = lines[0].replace("### ", "").strip()
            body = lines[1] if len(lines) > 1 else ""
            cat = parse_field(body, "Categoria")
            discs = split_items(parse_field(body, "Disciplinas Relacionadas").replace(";", ","))
            disc = discs[0] if discs else ""
            self.set_category(title, cat)
            for t in split_items(parse_field(body, "Termos Relacionados").replace(";", ",")):
                self.add_edge(
                    title, "relacionado a", t, disc, "DICIONARIO_GLOBAL", cat, None
                )
                count += 1
        return count

    def parse_indice_semantico(self) -> int:
        count = 0
        for code, dname in DISCIPLINES:
            disc = f"{code} {dname}"
            for folder in BASE.iterdir():
                if not folder.is_dir() or not folder.name.startswith(f"{code} "):
                    continue
                path = folder / "INDICE_SEMANTICO.md"
                if not path.exists():
                    continue
                text = normalize_raw(path.read_text(encoding="utf-8", errors="replace"))
                for part in re.split(r"\n(?=### )", text):
                    if not part.strip().startswith("### "):
                        continue
                    lines = part.split("\n", 1)
                    tema = lines[0].replace("### ", "").strip()
                    body = lines[1] if len(lines) > 1 else ""
                    self.set_category(tema, "Conceito")
                    for item in split_items(parse_field(body, "Conceitos relacionados")):
                        self.add_edge(
                            tema, "conecta", item, disc, "INDICE_SEMANTICO"
                        )
                        count += 1
                    for item in split_items(parse_field(body, "Doutrinas relacionadas")):
                        self.add_edge(
                            tema, "fundamentado em", item, disc, "INDICE_SEMANTICO"
                        )
                        count += 1
                    for item in split_items(parse_field(body, "Personagens relacionados")):
                        self.add_edge(
                            tema, "menciona", item, disc, "INDICE_SEMANTICO",
                            "Conceito", "Pessoa",
                        )
                        count += 1
        return count

    def parse_indice_global(self) -> int:
        """Registra nós do índice temático; arestas leves entre co-ocorrência."""
        text = normalize_raw(INDICE_FILE.read_text(encoding="utf-8", errors="replace"))
        count = 0
        current_section = ""
        section_items: list[str] = []
        discs: list[str] = []

        def flush_section() -> None:
            nonlocal count
            if not current_section or len(section_items) < 2:
                return
            disc = discs[0] if discs else ""
            anchor = current_section.title()
            for item in section_items[:30]:
                self.add_edge(
                    anchor, "associado a", item, disc, "INDICE_GLOBAL",
                    "Conceito", None,
                )
                count += 1

        for line in text.splitlines():
            if line.startswith("# ") and not line.startswith("## "):
                flush_section()
                sec = line[2:].strip()
                if sec.startswith("ÍNDICE") or sec.startswith("---"):
                    current_section = ""
                    continue
                current_section = sec
                section_items = []
                discs = []
                continue
            if line.startswith("## Disciplinas Relacionadas"):
                continue
            if line.startswith("- **") and " — " in line and current_section:
                m = re.match(r"- \*\*(\d+)\*\* — (.+)", line)
                if m:
                    discs.append(f"{m.group(1)} {m.group(2)}")
                continue
            if line.startswith("- ") and current_section:
                item = line[2:].strip()
                if item and item != "—":
                    section_items.append(item)
                    self.set_category(item, self.infer_category(item))

        flush_section()
        return count

    def _parse_kb_triple_line(self, line: str, default_fonte: str) -> int:
        count = 0
        disc_m = re.match(r"^- \[(\d{2} [^\]]+)\]\s*(.+)$", line.strip())
        disc = disc_m.group(1) if disc_m else ""
        content = disc_m.group(2) if disc_m else line.strip().lstrip("- ")

        # Pattern: **A** <tag> **B** (possibly multiple per line)
        for m in re.finditer(
            r"\*\*(.+?)\*\*\s*<([^>]+)>\s*\*\*(.+?)\*\*",
            content,
        ):
            src, tag, tgt = m.group(1).strip(), m.group(2).strip(), m.group(3).strip()
            rel = map_relation(tag)
            self.add_edge(src, rel, tgt, disc, default_fonte)
            count += 1

        # Pattern: **A & B**: description
        for m in re.finditer(r"\*\*(.+?)\*\*:\s*", content):
            pair = m.group(1).strip()
            if "&" in pair:
                parts = [p.strip() for p in pair.split("&")]
                for i in range(len(parts) - 1):
                    self.add_edge(parts[i], "conecta", parts[i + 1], disc, default_fonte)
                    count += 1

        # Pattern: **A** → **B** → **C**
        arrow_parts = re.findall(r"\*\*(.+?)\*\*", content)
        if "→" in content and len(arrow_parts) >= 2:
            for i in range(len(arrow_parts) - 1):
                self.add_edge(
                    arrow_parts[i], "conecta", arrow_parts[i + 1], disc, default_fonte
                )
                count += 1

        return count

    def parse_kb_relacionamentos(self) -> int:
        text = normalize_raw(KB_FILE.read_text(encoding="utf-8", errors="replace"))
        m = re.search(
            r"# RELACIONAMENTOS GLOBAIS\n+([\s\S]+?)(?=\n# |\Z)",
            text,
        )
        if not m:
            return 0
        count = 0
        section = "triplas"
        for line in m.group(1).splitlines():
            if line.startswith("## "):
                section = strip_accents(line[3:].strip().lower())
                continue
            if not line.strip().startswith("- "):
                continue
            if section.startswith("triplas") or "kb_master" in section:
                count += self._parse_kb_triple_line(line, "KB_BASICO_COMPLETO")
            elif "indice_semantico" in section or "temas semanticos" in section:
                # Handled by parse_indice_semantico; skip duplicate
                pass
        return count

    def parse_kb_entries(self) -> int:
        """Termos relacionados em entradas ### do KB consolidado."""
        text = normalize_raw(KB_FILE.read_text(encoding="utf-8", errors="replace"))
        count = 0
        title: str | None = None
        body_lines: list[str] = []
        for line in text.splitlines():
            if line.startswith("### "):
                if title:
                    body = "\n".join(body_lines)
                    fontes = parse_field(body, "Fontes")
                    disc = fontes.split(";")[0].strip() if fontes else ""
                    for t in split_items(
                        parse_field(body, "Termos relacionados").replace(";", ",")
                    ):
                        self.add_edge(title, "relacionado a", t, disc, "KB_BASICO_COMPLETO")
                        count += 1
                title = line[4:].strip()
                body_lines = []
            elif title:
                body_lines.append(line)
        return count

    def add_curated_examples(self) -> None:
        """Exemplos explícitos da especificação + arestas teológicas centrais."""
        curated = [
            ("Jesus Cristo", "relacionado a", "Reino de Deus", "11 Os Evangelhos", "curadoria", "Pessoa", "Conceito"),
            ("Moisés", "associado a", "Pentateuco", "06 Pentateuco", "curadoria", "Pessoa", "Livro Bíblico"),
            ("Gnosticismo", "contradiz", "Encarnação", "11 Os Evangelhos", "curadoria", "Heresia", "Conceito"),
            ("Jerusalém", "ocorre em", "Evangelhos", "11 Os Evangelhos", "curadoria", "Lugar", "Livro Bíblico"),
            ("Hermenêutica", "deriva de", "Exegese", "10 Hermenêutica", "curadoria", None, None),
            ("Inspiração Verbal", "fundamentado em", "Theopneustos", "10 Hermenêutica", "curadoria", None, None),
            ("João", "contradiz", "Gnosticismo", "11 Os Evangelhos", "curadoria", "Pessoa", "Heresia"),
            ("Adão", "deriva de", "Pecado Original", "07 Doutrinas Bíblicas do Velho Testamento", "curadoria", "Pessoa", None),
            ("Graça", "fundamentado em", "Salvação", "08 Teologia do Novo Testamento", "curadoria", None, None),
            ("Espírito Santo", "associado a", "Pneumatologia", "08 Teologia do Novo Testamento", "curadoria", None, None),
        ]
        for item in curated:
            src, rel, tgt, disc, fonte = item[:5]
            src_cat = item[5] if len(item) > 5 else None
            tgt_cat = item[6] if len(item) > 6 else None
            self.add_edge(src, rel, tgt, disc, fonte, src_cat, tgt_cat)


def main() -> None:
    g = GraphBuilder()
    g.preload_dic_categories()
    n_dic = g.parse_dic_global()
    n_ind = g.parse_indice_semantico()
    n_ig = g.parse_indice_global()
    n_kb_rel = g.parse_kb_relacionamentos()
    n_kb_ent = g.parse_kb_entries()
    g.add_curated_examples()

    edges = list(g.edges.values())
    node_degree: Counter[str] = Counter()
    rel_counter: Counter[str] = Counter()
    edge_pair_counter: Counter[tuple[str, str, str]] = Counter()

    for e in edges:
        node_degree[e.source] += 1
        node_degree[e.target] += 1
        rel_counter[e.relation] += 1
        edge_pair_counter[(e.source, e.relation, e.target)] += 1

    by_source: dict[str, list[Edge]] = defaultdict(list)
    for e in edges:
        by_source[e.source].append(e)

    lines: list[str] = [
        "---",
        'nivel: "Básico em Teologia"',
        "disciplinas_total: 12",
        f"nos_total: {len(g.nodes)}",
        f"arestas_total: {len(edges)}",
        "versao: 1.0.0",
        "fase: 2",
        "---",
        "",
        "# GRAPH_RELATIONSHIPS — Pastor IA",
        "",
        "Grafo semântico global do Curso Básico em Teologia, consolidado a partir de "
        "`KB_BASICO_COMPLETO.md`, `DICIONARIO_GLOBAL.md`, `INDICE_GLOBAL.md` e "
        "`INDICE_SEMANTICO.md`. Formato de triplas para GraphRAG e navegação na plataforma web.",
        "",
        "## Tipos de Relacionamento",
        "",
    ]
    for rel in sorted(ALLOWED_RELATIONS):
        lines.append(f"- **{rel}**")

    lines.extend([
        "",
        "## Ontologia de Nós",
        "",
    ])
    cat_counts = Counter(g.nodes.values())
    for cat, n in cat_counts.most_common():
        lines.append(f"- **{cat}**: {n} entidade(s)")

    lines.extend(["", "## Arestas Semânticas", ""])

    for src in sorted(by_source.keys(), key=lambda x: strip_accents(x).lower()):
        cat_src = g.nodes.get(src, "Conceito")
        lines.append(f"### {src}")
        lines.append(f"- **Categoria**: {cat_src}")
        lines.append("")
        for e in sorted(by_source[src], key=lambda x: (x.relation, strip_accents(x.target).lower())):
            cat_tgt = g.nodes.get(e.target, "Conceito")
            lines.extend([
                f"{e.source}",
                f"→ {e.relation}",
                f"→ {e.target}",
                "",
                f"- **Categoria origem**: {cat_src}",
                f"- **Categoria destino**: {cat_tgt}",
                f"- **Disciplina**: {e.discipline or '—'}",
                f"- **Fonte**: {e.fonte}",
                "",
            ])

    lines.extend(["---", "", "## Estatísticas", ""])
    lines.append(f"- **Total de nós**: {len(g.nodes)}")
    lines.append(f"- **Total de arestas**: {len(edges)}")
    lines.append(f"- **Fontes processadas**: DICIONARIO_GLOBAL ({n_dic}), INDICE_SEMANTICO ({n_ind}), INDICE_GLOBAL ({n_ig}), KB relacionamentos ({n_kb_rel}), KB entradas ({n_kb_ent})")
    lines.append("")
    lines.append("### Top 50 entidades mais conectadas")
    lines.append("")
    for name, deg in node_degree.most_common(50):
        lines.append(f"- **{name}** ({g.nodes.get(name, 'Conceito')}): {deg} conexão(ões)")
    lines.append("")
    lines.append("### Top 50 relacionamentos (triplas)")
    lines.append("")
    for (src, rel, tgt), n in edge_pair_counter.most_common(50):
        lines.append(f"- **{src}** → {rel} → **{tgt}**")

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    OUT_FILE.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Written: {OUT_FILE}")
    print(f"Nodes: {len(g.nodes)} | Edges: {len(edges)}")
    print(f"Sources: dic={n_dic} ind={n_ind} ig={n_ig} kb_rel={n_kb_rel} kb_ent={n_kb_ent}")


if __name__ == "__main__":
    main()
