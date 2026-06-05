# Pastor IA

Repositório de conhecimento teológico estruturado a partir das transcrições do **Curso Básico em Teologia** (Instituto Teológico Renacer), preparado para RAG, busca semântica e agentes conversacionais.

O padrão oficial de artefatos, formatação e governança está definido em [`PADRAO_OFICIAL_PASTOR_IA.md`](PADRAO_OFICIAL_PASTOR_IA.md).

---

# Status Atual do Projeto

## Curso Básico em Teologia

**Status:**  
Concluído (12/12 disciplinas)

**Disciplinas concluídas:**

* Introdução à Teologia
* Métodos de Estudos Bíblicos
* Homilética
* Arqueologia e Geografia 1
* Arqueologia e Geografia 2
* Pentateuco
* Doutrinas Bíblicas do Velho Testamento
* Teologia do Novo Testamento
* Livros Poéticos
* Hermenêutica
* Os Evangelhos
* Heresiologia

**Artefatos gerados por disciplina:**

* `KB_MASTER.md`
* `DOUTRINAS.md`
* `DICIONARIO.md`
* `VERSICULOS.md`
* `INDICE_SEMANTICO.md`

> **Nota:** A disciplina **05 Arqueologia e Geografia 2** possui apenas `KB_MASTER.md` (formato legado). As demais 11 disciplinas possuem o conjunto completo de cinco artefatos.

---

## Fases do Projeto

| Fase | Status | Descrição |
| :--- | :---: | :--- |
| **1A** | ✅ Concluída | Saneamento do repositório |
| **1B** | ✅ Concluída | Base de conhecimento por disciplina (Curso Básico) |
| **2** | 📋 Planejada | Auditoria e consolidação global |

Detalhes: [`ROADMAP.md`](ROADMAP.md) · Relatório da Fase 1B: [`RELATORIO_FINAL_FASE_1B.md`](RELATORIO_FINAL_FASE_1B.md)

---

## Estrutura

```
01 Básico em Teologia/
  ├── 01 Introdução a Teologia/
  ├── 02 Métodos de Estudos Bíblicos/
  ├── … (12 disciplinas)
  └── 12 Heresiologia/
      ├── Aula *.md          # transcrições-fonte
      ├── KB_MASTER.md
      ├── DOUTRINAS.md
      ├── DICIONARIO.md
      ├── VERSICULOS.md
      └── INDICE_SEMANTICO.md
```

---

## Documentação de Execução

* [`task.md`](task.md) — status operacional da Fase 1B
* [`walkthrough.md`](walkthrough.md) — registro por disciplina (commits, métricas, escopo)
