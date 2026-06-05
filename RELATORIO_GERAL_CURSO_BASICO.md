# RELATÓRIO GERAL — CURSO BÁSICO EM TEOLOGIA

**Projeto:** Pastor IA — Fase 1B  
**Data da auditoria:** 2026-06-04  
**Escopo:** Disciplinas 01–11 processadas (KB_MASTER gerado)  
**Método:** Contagem automatizada dos artefatos `DICIONARIO.md`, `DOUTRINAS.md`, `VERSICULOS.md`, `INDICE_SEMANTICO.md` e `KB_MASTER.md`; análise de sobreposição lexical entre disciplinas.

---

## 1. Resumo Executivo

O Curso **Básico em Teologia** possui **11 disciplinas com KB_MASTER** concluído, totalizando **159 aulas** analisadas. Dessas, **10 disciplinas** seguem o padrão completo de cinco artefatos oficiais. A disciplina **05 Arqueologia e Geografia 2** mantém apenas `KB_MASTER.md` (formato legado da Fase 1B inicial). A disciplina **12 Heresiologia** (28 aulas) ainda não foi processada.

A base acumulada contém **339 conceitos**, **98 doutrinas**, **326 versículos**, **219 personagens**, **74 eventos históricos** e **108 temas semânticos** — métricas extraídas exclusivamente dos artefatos locais padronizados.

---

## 2. Totais Consolidados

| Métrica | Quantidade | Observação |
| :--- | :---: | :--- |
| **Disciplinas processadas** | 11 | Com `KB_MASTER.md` |
| **Disciplinas com artefato completo (5/5)** | 10 | Exceto 05 (1/5) |
| **Total de aulas (disciplinas processadas)** | 159 | Soma das 11 disciplinas |
| **Total de KB_MASTER** | 11 | Um por disciplina processada |
| **Total de conceitos** | 339 | Tipo `conceito` em `DICIONARIO.md` |
| **Total de doutrinas** | 98 | Entradas `### Doutrina` em `DOUTRINAS.md` |
| **Total de versículos** | 326 | Entradas `###` em `VERSICULOS.md` |
| **Total de personagens** | 219 | Tipo `personagem` em `DICIONARIO.md` |
| **Total de eventos históricos** | 74 | Tipo `evento` em `DICIONARIO.md` |
| **Total de temas semânticos** | 108 | Entradas `###` em `INDICE_SEMANTICO.md` |

### Projeção do curso completo (incluindo pendências)

| Item | Processado | Pendente | Total previsto (12 disciplinas) |
| :--- | :---: | :---: | :---: |
| Disciplinas | 11 | 1 (Heresiologia) | 12 |
| Aulas | 159 | 28 | 187 |
| Artefatos completos (5×) | 10 | 2* | 12 |

\* 05 requer regeneração dos 4 artefatos faltantes; 12 ainda não iniciada.

---

## 3. Inventário por Disciplina

| Cód. | Disciplina | Aulas | Artefatos | Conceitos | Doutrinas | Versículos | Personagens | Eventos | Temas | Professor (KB) |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| 01 | Introdução a Teologia | 7 | 5/5 | 10 | 5 | 8 | 11 | 1 | 6 | Alex Martins |
| 02 | Métodos de Estudos Bíblicos | 6 | 5/5 | 9 | 4 | 11 | 3 | 0 | 5 | Alex Martins |
| 03 | Homilética | 17 | 5/5 | 14 | 3 | 11 | 9 | 0 | 4 | Alex Martins |
| 04 | Arqueologia e Geografia 1 | 16 | 5/5 | 10 | 3 | 11 | 10 | 0 | 3 | Alex Martins |
| 05 | Arqueologia e Geografia 2 | 14 | **1/5** | — | — | — | — | — | — | Alex Martins* |
| 06 | Pentateuco | 15 | 5/5 | 46 | 12 | 37 | 25 | 3 | 13 | Pastor Carvalho Júnior |
| 07 | Doutrinas Bíblicas do VT | 19 | 5/5 | 38 | 13 | 47 | 34 | 6 | 13 | Pastor Thiago Domingos |
| 08 | Teologia do Novo Testamento | 14 | 5/5 | 47 | 15 | 77 | 29 | 12 | 15 | não informado |
| 09 | Livros Poéticos | 12 | 5/5 | 36 | 14 | 50 | 33 | 16 | 14 | Natã Maestrel |
| 10 | Hermenêutica | 14 | 5/5 | 65 | 14 | 27 | 36 | 13 | 16 | Pastor Carvalho Júnior |
| 11 | Os Evangelhos | 25 | 5/5 | 64 | 15 | 47 | 29 | 23 | 19 | Pastor Tiago Domínguez |

**Nota sobre 05:** Possui `KB_MASTER.md` extenso (formato legado, sem frontmatter padronizado completo), com ~7 conceitos principais, ~14 definições, ~40 personagens e ~20 eventos embutidos no próprio KB — não contabilizados nos totais acima por ausência de `DICIONARIO.md`.

---

## 4. Rankings

### 4.1 Disciplinas com mais conceitos

| Pos. | Disciplina | Conceitos |
| :---: | :--- | :---: |
| 1 | 10 Hermenêutica | 65 |
| 2 | 11 Os Evangelhos | 64 |
| 3 | 08 Teologia do Novo Testamento | 47 |
| 4 | 06 Pentateuco | 46 |
| 5 | 07 Doutrinas Bíblicas do VT | 38 |
| 6 | 09 Livros Poéticos | 36 |
| 7 | 03 Homilética | 14 |
| 8 | 01 Introdução a Teologia | 10 |
| 9 | 04 Arqueologia e Geografia 1 | 10 |
| 10 | 02 Métodos de Estudos Bíblicos | 9 |

### 4.2 Disciplinas com mais doutrinas

| Pos. | Disciplina | Doutrinas |
| :---: | :--- | :---: |
| 1 | 08 Teologia do Novo Testamento | 15 |
| 1 | 11 Os Evangelhos | 15 |
| 3 | 09 Livros Poéticos | 14 |
| 3 | 10 Hermenêutica | 14 |
| 5 | 07 Doutrinas Bíblicas do VT | 13 |
| 6 | 06 Pentateuco | 12 |
| 7 | 01 Introdução a Teologia | 5 |
| 8 | 02 Métodos de Estudos Bíblicos | 4 |
| 9 | 03 Homilética | 3 |
| 9 | 04 Arqueologia e Geografia 1 | 3 |

### 4.3 Disciplinas com mais versículos

| Pos. | Disciplina | Versículos |
| :---: | :--- | :---: |
| 1 | 08 Teologia do Novo Testamento | 77 |
| 2 | 09 Livros Poéticos | 50 |
| 3 | 07 Doutrinas Bíblicas do VT | 47 |
| 3 | 11 Os Evangelhos | 47 |
| 5 | 06 Pentateuco | 37 |
| 6 | 10 Hermenêutica | 27 |
| 7 | 01 Introdução a Teologia | 8 |
| 8 | 02 Métodos de Estudos Bíblicos | 11 |
| 8 | 03 Homilética | 11 |
| 8 | 04 Arqueologia e Geografia 1 | 11 |

### 4.4 Disciplinas mais conectadas

*Índice de conectividade = soma das conexões cruzadas por conceitos e personagens compartilhados (títulos idênticos em `DICIONARIO.md` de 2+ disciplinas).*

| Pos. | Disciplina | Índice | Conexões notáveis |
| :---: | :--- | :---: | :--- |
| 1 | 07 Doutrinas Bíblicas do VT | 39 | Adão, Moisés, Davi, Jeremias; justificação, graça, santificação |
| 2 | 08 Teologia do Novo Testamento | 36 | Jesus Cristo, Paulo, Pedro; tricotomia, regeneração |
| 3 | 09 Livros Poéticos | 30 | Adão, Eva, José; tipologia; Sl 51 compartilhado |
| 4 | 10 Hermenêutica | 27 | Moisés, Davi, Paulo; exegese, hermenêutica, 2 Tm 3:16 |
| 5 | 06 Pentateuco | 20 | Adão, Moisés, José; criação, aliança |
| 6 | 11 Os Evangelhos | 9 | Justificação, kenosis; Jo 1:1, Jo 3:16, Mt 7 |
| 7 | 01 Introdução a Teologia | 4 | Kenosis; Gn 1:1 |
| 8 | 02 Métodos de Estudos Bíblicos | 3 | Axioma; inspiração bíblica |
| 8 | 03 Homilética | 3 | Hermenêutica, exegese |
| 8 | 04 Arqueologia e Geografia 1 | 3 | Jonas; Gn 1:1 |
| — | 05 Arqueologia e Geografia 2 | 0 | Sem `DICIONARIO.md` — isolada do grafo local |

**Hubs temáticos identificados:**
- **07 + 08:** eixo doutrinário central (VT → NT)
- **10 + 11:** eixo interpretativo-evangélico
- **06 + 07:** eixo pentateucal-doutrinário
- **04 + 05:** eixo geográfico (05 legado desconectado)

---

## 5. Duplicidades e Sobreposições

### 5.1 Conceitos com título idêntico em múltiplas disciplinas

| Conceito | Disciplinas | Risco |
| :--- | :--- | :--- |
| Justificação | 07, 08, 11 | Alto — definições convergentes mas contextos distintos |
| Hermenêutica | 03, 10 | Médio — 03 introduz; 10 aprofunda |
| Exegese | 03, 10 | Médio — mesma relação |
| Graça | 07, 08 | Médio — VT soteriologia vs. teologia paulina |
| Regeneração | 07, 08 | Médio | 
| Santificação | 07, 08 | Médio |
| Tipologia | 07, 09 | Baixo — escopos diferentes |
| Tricotomia | 07, 08 | Médio — antropologia compartilhada |
| Kenosis | 01, 11 | Baixo — introdução vs. cristologia joanina |
| Axioma | 02, 10 | Médio — método vs. hermenêutica |

### 5.2 Doutrinas com nomenclatura sobreposta

| Tema doutrinário | Ocorrências | Disciplinas |
| :--- | :--- | :--- |
| Inspiração Bíblica / das Escrituras / Verbal | 6+ variações | 02, 06, 07, 09, 10 |
| Criação | 2 | 06, 07 |
| Deus (Teontologia) | 2 | 07, 08 |
| Providência | 2 | 06, 09 |
| Perseverança | 2 | 09, 11 |
| Igreja / Eclesiologia | 3 | 08, 11 (+ Homilética implícita) |

### 5.3 Versículos catalogados em mais de uma disciplina

| Referência | Disciplinas |
| :--- | :--- |
| Gênesis 1:1 | 01, 04, 06, 08 |
| Gênesis 1:26 | 01, 06 |
| 2 Timóteo 3:16 | 06, 10 |
| Salmo 51 | 07, 09 |
| Mateus 7 | 07, 11 |
| João 1:1 | 07, 11 |
| João 3:16 | 07, 11 |
| João 16:13 | 08, 10 |
| Efésios 5:18 | 07, 08 |
| 1 Tessalonicenses 5:23 | 07, 08 |
| Tito 2:11 | 07, 08 |

### 5.4 Personagens recorrentes (3+ disciplinas)

| Personagem | Disciplinas | Total |
| :--- | :--- | :---: |
| Adão | 06, 07, 08, 09, 10 | 5 |
| Moisés | 06, 07, 08, 09, 10 | 5 |
| Davi | 07, 08, 09, 10 | 4 |
| Eva | 06, 07, 09 | 3 |
| Jeremias | 07, 08, 09 | 3 |
| Jesus Cristo | 07, 08, 09 | 3 |
| Jonas | 02, 04, 10 | 3 |
| José | 06, 07, 09 | 3 |
| Paulo | 08, 09, 10 | 3 |
| Pedro | 08, 09, 10 | 3 |
| Isaías | 07, 08, 10 | 3 |
| Constantino | 01, 07, 11 | 3 |

### 5.5 Termos equivalentes e variações de transcrição (risco de nó duplicado)

Detectados nos artefatos via campos `Palavras-chave equivalentes` e erros de transcrição Whisper:

| Família | Variantes encontradas | Disciplinas afetadas |
| :--- | :--- | :--- |
| Instituto Renacer | Renacê, Renacer, Renaceno, Renaciano, Renasem | 10, 11 |
| Personagens históricos | Gênsabele / Jezabel; Carvalho Junho / Júnior | 05, 06, 10 |
| Geografia | Coelhada / Goel; Aemia Paputoliva / Aelia Capitolina | 04, 05 |
| Teologia | guinoticismo / gnosticismo | 11 |
| Hermenêutica | imeneutica / hermenêutica / exigência / exegese | 10 |
| Autor | Thiago Domíngus / Domínguez | 11 |

---

## 6. Possíveis Fusões Futuras (recomendações — não executadas)

| Cluster | Disciplinas | Justificativa | Prioridade |
| :--- | :--- | :--- | :---: |
| **Geografia Bíblica** | 04 + 05 | Continuidade temática; 05 legado deve ser reprocessada no padrão 5 artefatos | Alta |
| **Soteriologia** | 07 + 08 + 11 | Justificação, graça, regeneração, expiação recorrentes | Alta |
| **Bibliologia / Inspiração** | 02 + 06 + 07 + 09 + 10 | Mesma doutrina com 6 nomenclaturas | Alta |
| **Cristologia** | 08 + 11 + 01 | Cristo, kenosis, quatro ofícios, teontologia | Média |
| **Interpretação Bíblica** | 02 + 03 + 10 + 09 | Método, homilética, hermenêutica, poesia | Média |
| **Antropologia** | 07 + 08 | Tricotomia, homem carnal/espiritual | Média |
| **Pentateuco–Doutrinas VT** | 06 + 07 | Criação, aliança, hamartologia compartilhados | Baixa |

**Fusão sugerida para artefatos globais (Fase futura, não executada nesta auditoria):**
- `DICIONARIO_GLOBAL`: unificar ~339 conceitos com UUID e aliases (Goel/Coelhada, Renacer/Renacê)
- `GRAPH_RELATIONSHIPS`: priorizar arestas 07↔08↔11 e 06↔07↔09

---

## 7. Lacunas e Inconsistências

| Lacuna | Impacto | Ação recomendada |
| :--- | :--- | :--- |
| 05 sem 4 artefatos | Disciplina isolada no grafo; métricas incompletas | Reprocessar Fase 1B completa |
| 12 Heresiologia pendente | 28 aulas (~15% do curso) ausentes | Próxima disciplina na fila |
| Professores não informados (08) | Metadado YAML incompleto | Revisar transcrições |
| Disciplinas 01–04 com poucos eventos | `evento=0` em 02, 03, 04 | Aceitável pelo conteúdo; revisar se aulas citam eventos |
| Encoding UTF-8 em 05 KB legado | Caracteres corrompidos (`BÃ­blica`) | Normalizar na regeneração |
| Contagem de versículos sem normalização canônica | Gn 1:1 vs. Gênesis 1:1 podem duplicar no global | Implementar IDs `GEN_1_1` (PADRAO_OFICIAL) |

---

## 8. Distribuição por Professor

| Professor | Disciplinas | Aulas | Conceitos* |
| :--- | :---: | :---: | :---: |
| Alex Martins | 01, 02, 03, 04, 05 | 59 | 43 (+05 legado) |
| Pastor Carvalho Júnior | 06, 10 | 29 | 111 |
| Pastor Thiago Domingos | 07 | 19 | 38 |
| Natã Maestrel | 09 | 12 | 36 |
| Pastor Tiago Domínguez | 11 | 25 | 64 |
| Não informado | 08 | 14 | 47 |

\* Conceitos apenas de disciplinas com `DICIONARIO.md`.

---

## 9. Parecer Técnico — Maturidade da Base de Conhecimento

### 9.1 Avaliação geral: **MÉDIA-ALTA (72/100)**

A base de conhecimento do Curso Básico encontra-se em estágio **operacional para RAG local por disciplina**, com cobertura substancial de conteúdo teológico fundamental, porém **ainda imatura para fusão global** sem pipeline de normalização.

### 9.2 Pontos fortes

1. **Cobertura disciplinar:** 92% das disciplinas planejadas (11/12) possuem KB_MASTER; 83% (10/12) no padrão completo de 5 artefatos.
2. **Volume significativo:** 339 conceitos e 326 versículos catalogados com contexto e uso teológico — adequado para chunking semântico por disciplina.
3. **Estrutura padronizada:** Frontmatter YAML, seções fixas do `PADRAO_OFICIAL_PASTOR_IA.md` e artefatos paralelos (`DOUTRINAS`, `DICIONARIO`, `VERSICULOS`, `INDICE_SEMANTICO`) facilitam parseamento.
4. **Hubs bem formados:** 07 (Doutrinas VT) e 08 (Teologia NT) funcionam como eixos de conectividade natural — prontos para GraphRAG.
5. **Riqueza narrativa:** 11 Os Evangelhos e 09 Livros Poéticos elevam personagens (219) e eventos (74) para nível útil em busca por entidade.

### 9.3 Pontos de atenção

1. **Isolamento da disciplina 05:** KB legado sem interoperabilidade com o grafo local.
2. **Duplicidade doutrinária:** Inspiração bíblica aparece em 5+ disciplinas com nomenclaturas distintas — exigirá desambiguação no `DICIONARIO_GLOBAL`.
3. **Conectividade desigual:** Disciplinas introdutórias (01–04) têm índice baixo (3–4) — esperado, mas limitam busca transversal.
4. **Ausência de IDs canônicos:** Versículos e entidades sem `GEN_1_1` / UUID — risco de nós duplicados no grafo.
5. **Erros de transcrição:** Whisper preservados nos artefatos (ex.: Gênsabele, guinoticismo) — degradam embeddings se não normalizados.

### 9.4 Prontidão por sistema de IA (conforme PADRAO_OFICIAL)

| Sistema | Prontidão | Justificativa |
| :--- | :---: | :--- |
| **RAG por disciplina** | Alta | Artefatos estruturados e autocontidos |
| **RAG global** | Média | Duplicidades e 05 legado bloqueiam consolidação limpa |
| **GraphRAG** | Média-Baixa | Sem `GRAPH_RELATIONSHIPS.md`; conectividade inferida apenas por título |
| **GPT/Assistente com filtro** | Alta | YAML frontmatter permite filtro por disciplina |
| **Busca semântica global** | Média | Requer ETL de normalização + deduplicação |

### 9.5 Recomendações prioritárias (sem execução nesta auditoria)

1. **Reprocessar 05 Arqueologia e Geografia 2** no padrão 5 artefatos.
2. **Concluir 12 Heresiologia** — maior volume pendente (28 aulas).
3. **Pipeline de normalização** antes de `DICIONARIO_GLOBAL`: aliases, versículos canônicos, correção OCR.
4. **Matriz de fusão doutrinária** inspirada na seção 6 deste relatório.
5. **Manter restrição atual:** não gerar artefatos globais até 12/12 disciplinas completas.

---

## 10. Conclusão

A Fase 1B do Pastor IA consolidou uma base de conhecimento **robusta e estruturada** para 11 disciplinas do Curso Básico, com **159 aulas** transformadas em **1.140 entidades catalogadas** (soma de conceitos, doutrinas, versículos, personagens, eventos e temas). A maturidade é **suficiente para uso disciplinar imediato**, mas **insuficiente para consolidação global automática** sem resolver duplicidades, regenerar a disciplina 05 e completar a Heresiologia.

**Próximo marco recomendado:** 12/12 disciplinas com 5 artefatos → então iniciar `DICIONARIO_GLOBAL` e `GRAPH_RELATIONSHIPS`.

---

*Relatório gerado por auditoria automatizada sobre os artefatos em `01 Básico em Teologia/`. Nenhum artefato global foi criado nesta etapa.*
