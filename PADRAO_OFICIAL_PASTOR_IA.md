# PADRÃO OFICIAL DE ARQUITETURA DE CONHECIMENTO E RAG — PASTOR IA

Este documento define o padrão oficial de governança, formatação, extração e mapeamento de dados teológicos no repositório [Pastor IA](file:///c:/src/projects/pastor_ia/). A arquitetura aqui definida visa maximizar a eficiência de sistemas de busca semântica, agentes conversacionais baseados em LLMs, indexadores vetoriais tradicionais (RAG) e grafos de conhecimento semânticos (GraphRAG).

---

## 1. Auditoria Comparativa do KB_MASTER Existente
Atualmente, existe apenas um arquivo `KB_MASTER.md` implementado no repositório, correspondente à disciplina [05 Arqueologia e Geografia 2](file:///c:/src/projects/pastor_ia/01%20B%C3%A1sico%20em%20Teologia/05%20Arqueologia%20e%20Geografia%202/KB_MASTER.md).

### Informações que aparecem e devem constar em todos os KB_MASTERs de Disciplinas:
- **Identificação da Disciplina e Nível**: Definição do contexto letivo (Básico, Médio, Bacharel) e módulo correspondente.
- **Estruturação Temática de Visão Geral**: Tema principal, objetivos de aprendizagem e um resumo executivo abrangente.
- **Mapeamento de Conhecimento Fundamental**: Separação clara de termos, conceitos, definições de termos teológicos, doutrinas correlatas, personagens envolvidos e eventos históricos.
- **Fundamentação Bíblica com Contexto e Uso**: Para cada versículo referenciado nas aulas, o mapeamento exaustivo do contexto histórico/literário e a aplicação dogmática dada na aula.
- **Matriz de Relacionamentos**: Conexões lógicas de causa, efeito e tipologia entre entidades teológicas.
- **Tabela de Controvérsias e Heresias**: Registro de debates teológicos legítimos e os desvios heréticos condenados.
- **Aplicações Práticas**: Lições de vida, aconselhamento e liderança cristã extraídas do conteúdo.
- **Indexação por Palavras-Chave**: Lista abrangente de tags e entidades.

---

## 2. Seções a serem Padronizadas nos KB_MASTERs
Para garantir que o parseador RAG (Python/LangChain/LlamaIndex) faça a extração correta de dados sem ruído, os títulos e subtítulos de cada `KB_MASTER.md` individual de disciplina deverão seguir estritamente a seguinte estrutura de cabeçalhos Markdown:

1. `# [CÓDIGO - NOME DA DISCIPLINA]` (H1)
2. `# VISÃO GERAL` (H1)
   - `## Tema Principal` (H2)
   - `## Objetivos` (H2)
   - `## Resumo Executivo` (H2)
3. `# CONHECIMENTO FUNDAMENTAL` (H1)
   - `## Conceitos Principais` (H2)
   - `## Definições` (H2)
   - `## Termos Teológicos` (H2)
   - `## Doutrinas` (H2)
   - `## Personagens Bíblicos` (H2)
   - `## Eventos Históricos` (H2)
4. `# FUNDAMENTAÇÃO BÍBLICA` (H1)
   - Onde cada versículo deve ser estruturado em uma lista com a sintaxe:
     `* **[Livro Capítulo:Versículo]**`
     - `- *Contexto*: [Detalhamento do contexto]`
     - `- *Uso Teológico*: [Aplicação hermenêutica dada na aula]`
5. `# RELACIONAMENTOS` (H1)
6. `# CONTROVÉRSIAS` (H1)
7. `# HERESIAS RELACIONADAS` (H1)
8. `# APLICAÇÕES` (H1)
9. `# PALAVRAS-CHAVE` (H1)

---

## 3. Campos Extras Recomendados
Para otimizar a indexação por modelos de linguagem e bancos de dados vetoriais/grafos, propõe-se a inclusão de três novos campos técnicos:

1. **Metadados YAML (Frontmatter)**: Injetado no topo absoluto de cada arquivo para filtros rápidos de banco de dados (ex: por nível, professor ou quantidade de aulas).
2. **Entidades com IDs Únicos (Entity UUIDs)**: Anotação de termos e personagens recorrentes com IDs padronizados de forma a evitar que erros de digitação ou variações (ex: "Alexandre o Grande", "Alexandre Magno", "macedônico") gerem nós duplicados no grafo de conhecimento.
3. **Referências Bíblicas Normalizadas (Canonical Scripture References)**: Formato uniforme (ex: `GEN_12_6` ou `DT_28_1`) que permite indexação determinística das passagens bíblicas, ligando automaticamente diferentes aulas ao mesmo versículo.

---

## 4. Proposta de Estrutura Única dos 4 Artefatos de Conhecimento

### A. KB_MASTER.md (Estrutura Local por Disciplina)
Localizado na pasta de cada disciplina. Serve como o repositório consolidado do minicurso.
```markdown
---
nivel: "Básico em Teologia"
disciplina_id: "05"
disciplina_nome: "Arqueologia e Geografia 2"
professor: "Alex Martins"
aulas_total: 14
versao: 1.0.0
---

# KB_MASTER: Arqueologia e Geografia Bíblica 2

# VISÃO GERAL
## Tema Principal
...
## Objetivos
...
## Resumo Executivo
...

# CONHECIMENTO FUNDAMENTAL
## Conceitos Principais
...
## Definições
...
## Termos Teológicos
...
## Doutrinas
...
## Personagens Bíblicos
...
## Eventos Históricos
...

# FUNDAMENTAÇÃO BÍBLICA
* **[Referência Bíblica Canônica]**
  - *Contexto*: ...
  - *Uso Teológico*: ...

# RELACIONAMENTOS
- **[Entidade A]** <relacao> **[Entidade B]**: Explicação da relação.

# CONTROVÉRSIAS
- **[Tema da Divergência]**: Posicionamento A vs. Posicionamento B.

# HERESIAS RELACIONADAS
- **[Nome do Desvio]**: Descrição e refutação bíblica apresentada.

# APLICAÇÕES
- **[Aplicação Prática]**: Resumo de aplicação à liderança ou vida devocional.

# PALAVRAS-CHAVE
[Palavra-chave 1, Palavra-chave 2, ...]
```

### B. DICIONARIO_GLOBAL.md (Raiz do Projeto)
Consolida todas as definições e termos teológicos de todas as disciplinas em ordem alfabética para busca rápida e resolução de termos.
```markdown
# DICIONÁRIO GLOBAL — PASTOR IA

Este arquivo consolida e desambígua todos os termos teológicos, históricos e geográficos identificados nas disciplinas.

## A
### Aelia Capitolina
- **Definição**: Nome dado a Jerusalém pelo imperador Adriano em 135 d.C. para apagar a identidade judaico-cristã.
- **Fontes**: [Arqueologia e Geografia 2 (Aula 11)](file:///c:/src/projects/pastor_ia/01%20B%C3%A1sico%20em%20Teologia/05%20Arqueologia%20e%20Geografia%202/Aula%2011%20-%20Arqueologia%20e%20Geografia%202%20-%20Curso%20de%20Teologia%20B%C3%A1sico%20-%201920x1080%203248K.md#L3)
- **Sinônimos**: Aemia Paputoliva, Jerusalém Romana.

## G
### Goel
- **Definição**: O resgatador de sangue; parente encarregado de vingar a morte de um familiar.
- **Fontes**: [Arqueologia e Geografia 2 (Aula 05)](file:///c:/src/projects/pastor_ia/01%20B%C3%A1sico%20em%20Teologia/05%20Arqueologia%20e%20Geografia%202/Aula%2005%20-%20Arqueologia%20e%20Geografia%202%20-%20Curso%20de%20Teologia%20B%C3%A1sico%20-%201920x1080%202540K.md#L15)
- **Sinônimos**: Coelhada (erro de transcrição fonética), Vingador de Sangue.
```

### C. INDICE_GLOBAL.md (Raiz do Projeto)
Mapeia recursivamente todas as pastas, arquivos de aulas, extensões, quantidades de arquivos, contagens de tokens aproximadas e o status de completude da biblioteca.
```markdown
# ÍNDICE GLOBAL DE CONHECIMENTO — PASTOR IA

## Mapeamento de Diretórios Acadêmicos

### 1. Básico em Teologia
- **Status Geral**: 92% Completo (transcrições brutas de 12 disciplinas).

| Código | Disciplina | Qtd. Aulas | Formato | Status | KB_MASTER |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 01 | Introdução à Teologia | 7 | .md | Incompleto | [ ] Não Iniciado |
| 02 | Métodos de Estudos Bíblicos | 6 | .md | Completo | [ ] Não Iniciado |
| 03 | Homilética | 17 | .md | Completo | [ ] Não Iniciado |
| 04 | Arqueologia e Geografia 1 | 16 | .md | Completo | [ ] Não Iniciado |
| 05 | Arqueologia e Geografia 2 | 14 | .md | Completo | [x] Implementado |
| 06 | Pentateuco | 15 | .txt | Erro Extensao | [ ] Não Iniciado |
| 07 | Doutrinas Bíblicas do VT | 19 | .md | Duplicado | [ ] Não Iniciado |
| 08 | Teologia do NT | 14 | .md | Completo | [ ] Não Iniciado |
| 09 | Livros Poéticos | 12 | .md | Completo | [ ] Não Iniciado |
| 10 | Hermenêutica | 14 | .md | Completo | [ ] Não Iniciado |
| 11 | Os Evangelhos | 25 | .md | Completo | [ ] Não Iniciado |
| 12 | Heresiologia | 28 | .md | Completo | [ ] Não Iniciado |

### 2. Médio em Teologia
- **Status Geral**: 0% (Vazio, apenas placeholders).

### 3. Bacharel em Teologia
- **Status Geral**: 0% (Vazio, apenas placeholders).
```

### D. GRAPH_RELATIONSHIPS.md (Raiz do Projeto)
Define as arestas e nós formais em formato interpretável para motores de GraphRAG (como Neo4j, LlamaIndex, ou LangChain Graphs).
```markdown
# MAPEAMENTO DE RELACIONAMENTOS SEMÂNTICOS (GRAPH) — PASTOR IA

Este arquivo define a ontologia e as arestas de relacionamento entre entidades do repositório para sistemas GraphRAG.

## Ontologia de Nós
- **(:Personagem)**: Indivíduo bíblico, teólogo ou figura histórica.
- **(:Conceito)**: Termo doutrinário, filosófico ou metodológico.
- **(:Local)**: Ponto geográfico, cidade ou relevo físico.
- **(:Evento)**: Acontecimento histórico ou bíblico temporal.
- **(:Passagem)**: Versículo ou capítulo da Bíblia canônica.

## Definição de Arestas e Triplas Semânticas

### Exemplo: Monte Moriah
- `(:Local {nome: "Monte Moriah"}) -[:PALCO_DE]-> (:Evento {nome: "Sacrifício de Isaque"})`
- `(:Local {nome: "Monte Moriah"}) -[:PALCO_DE]-> (:Evento {nome: "Parada do Anjo Destruidor"})`
- `(:Local {nome: "Monte Moriah"}) -[:LOCAL_DE]-> (:Conceito {nome: "Templo de Salomão"})`
- `(:Personagem {nome: "Abraão"}) -[:LIDEROU]-> (:Evento {nome: "Sacrifício de Isaque"})`

### Exemplo: Samaria e Sargon II
- `(:Personagem {nome: "Sargon II"}) -[:CONQUISTOU]-> (:Local {nome: "Samaria"})`
- `(:Personagem {nome: "Sargon II"}) -[:DECRETOU_A_MISTURA_DE]-> (:Conceito {nome: "Sincretismo Samaritano"})`
- `(:Conceito {nome: "Sincretismo Samaritano"}) -[:GEROU_OPOSICAO_A]-> (:Personagem {nome: "Neemias"})`
```

---

## 5. Avaliação Técnica de Sistemas de IA

### A. RAG Tradicional (Vetorial)
* **Adequação**: **Média**.
* **Motivo**: A estrutura atual de arquivos markdown longos, cheios de erros ortográficos de Whisper (por ex: "alusto estronde" no lugar de "Augustus Strong" e "Gênsabele" no lugar de "Jezabel"), degrade os resultados da busca por similaridade de cosseno de embeddings. Palavras com erros fonéticos geram embeddings distantes dos correspondentes corretos.
* **Solução**: Implementar um pipeline de ETL antes da vetorização para normalizar o texto e aplicar busca híbrida (Dense Embeddings + BM25 lexicais).

### B. GraphRAG
* **Adequação**: **Fraca (imediata), Excelente (com padronização)**.
* **Motivo**: Atualmente, sem o arquivo `GRAPH_RELATIONSHIPS.md`, um motor GraphRAG teria que extrair entidades a partir do texto bruto com erros fonéticos, gerando múltiplos nós duplicados e isolados para a mesma entidade teológica.
* **Solução**: O arquivo `GRAPH_RELATIONSHIPS.md` fornecerá um dicionário determinístico de entidades e arestas, resolvendo duplicatas e unificando o grafo de conhecimento com 100% de consistência.

### C. GPT Personalizado / OpenAI Assistants
* **Adequação**: **Boa**.
* **Motivo**: O formato Markdown hierárquico é facilmente consumido na janela de contexto dos modelos GPT-4o.
* **Gargalo**: Sem cabeçalhos de metadados Frontmatter em formato YAML nos arquivos de aula, o assistente não consegue aplicar filtros determinísticos precisos (ex: "busque apenas no nível Básico").

### D. Busca Semântica
* **Adequação**: **Média**.
* **Solução**: A busca semântica depende da similaridade vetorial dos chunks. A padronização proposta (YAML metadados + tabelas de conceitos) garantirá que a busca encontre os blocos teológicos consolidados corretos, mesmo que a transcrição original da aula contenha alguma imperfeição fonética local.

### E. Plataforma Web
* **Adequação**: **Excelente**.
* **Motivo**: O Markdown limpo e padronizado permite renderização imediata com bibliotecas como `react-markdown` ou `MDX` em interfaces Next.js. A estrutura de subpastas facilita a criação de rotas dinâmicas como `/cursos/[nivel]/[disciplina]/[aula]`.

---

## 6. Recomendações de Transição de KB_MASTER para Padrão Geral
1. **Script de Data Cleanup**: Desenvolver um script Python utilizando expressões regulares e chamadas de API (GPT-4o/Gemini) para normalizar a ortografia das aulas e converter arquivos `.txt` em `.md`.
2. **Injetor de YAML**: Automatizar a inserção de metadados no início de cada aula.
3. **Mapeamento Incremental**: Criar os KB_MASTERs de cada uma das disciplinas seguindo o padrão oficial do repositório.
