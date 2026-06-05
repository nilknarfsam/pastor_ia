# ROADMAP — Pastor IA

Planejamento de fases do projeto de arquitetura de conhecimento teológico.

Padrão de referência: [`PADRAO_OFICIAL_PASTOR_IA.md`](PADRAO_OFICIAL_PASTOR_IA.md)

---

## FASE 1A — Saneamento

**Status:** ✅ Concluída

**Objetivos:**

* Organização inicial do repositório e das transcrições
* Padronização de estrutura de pastas por nível e disciplina
* Definição do padrão oficial de artefatos (`PADRAO_OFICIAL_PASTOR_IA.md`)
* Preparação do material-fonte (aulas em Markdown) para extração

---

## FASE 1B — Geração da Base de Conhecimento por Disciplina

**Status:** ✅ Concluída

**Objetivos:**

* Gerar, por disciplina do **Curso Básico em Teologia**, os cinco artefatos oficiais:
  * `KB_MASTER.md`
  * `DOUTRINAS.md`
  * `DICIONARIO.md`
  * `VERSICULOS.md`
  * `INDICE_SEMANTICO.md`
* Extrair conteúdo exclusivamente das transcrições das aulas
* Registrar métricas e commits por disciplina (`walkthrough.md`, `task.md`)

**Resultado:**

* **12/12 disciplinas** com `KB_MASTER.md`
* **11/12 disciplinas** com conjunto completo (5/5 artefatos)
* **187 aulas** · **56 artefatos** padronizados · ver [`RELATORIO_FINAL_FASE_1B.md`](RELATORIO_FINAL_FASE_1B.md)

**Pendência herdada para Fase 2:**

* Reprocessar **05 Arqueologia e Geografia 2** (apenas `KB_MASTER.md` legado)

---

## FASE 2 — Auditoria e Consolidação Global

**Status:** 📋 Planejada

**Objetivos:**

Consolidar o conhecimento das 12 disciplinas do Curso Básico em artefatos na raiz do projeto, com deduplicação, normalização e grafo semântico.

| Artefato | Descrição |
| :--- | :--- |
| **`KB_BASICO_COMPLETO.md`** | KB unificado do Curso Básico com índice por disciplina e visão panorâmica |
| **`DICIONARIO_GLOBAL.md`** | Dicionário alfabético global com desambiguação e fontes |
| **`INDICE_GLOBAL.md`** | Mapa recursivo do repositório, status e métricas |
| **`GRAPH_RELATIONSHIPS.md`** | Ontologia e arestas para GraphRAG (Neo4j, LlamaIndex, etc.) |

**Entregas preparatórias:**

* Auditoria de duplicatas e conflitos terminológicos
* Normalização de erros fonéticos das transcrições
* Completar artefatos da disciplina 05
* Scripts de validação de schema e contagem

**Restrições até conclusão da Fase 2:**

* Não iniciar plataforma web
* Não deploy de busca semântica em produção

---

## Fases Futuras (rascunho)

| Fase | Foco |
| :--- | :--- |
| **3** | Pipeline RAG (ETL, chunking, embeddings híbridos) |
| **4** | Plataforma web e APIs de consulta |
| **5** | Cursos Médio e Bacharel em Teologia |

---

## Histórico de marcos

| Data | Marco |
| :--- | :--- |
| 2026-06-04 | Encerramento oficial da Fase 1B (12 disciplinas, Curso Básico) |
| 2026-06-04 | Última disciplina processada: **12 Heresiologia** (`1eea9a9`) |
