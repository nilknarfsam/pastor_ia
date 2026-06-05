# Walkthrough — Pastor IA

Registro de execução da **Fase 1B: Geração de Base de Conhecimento por Disciplina** e da **Fase AUDIO_OVERVIEW**.

---

## Fase AUDIO_OVERVIEW — Curso Básico (12 disciplinas)

**Data**: 2026-06-04  
**Objetivo**: Gerar `AUDIO_OVERVIEW.md` em narrativa contínua para ElevenLabs (estilo NotebookLM Audio Overview)  
**Fontes**: `KB_MASTER.md` e transcrições de cada disciplina (sem conhecimento externo)  
**Áudio**: não gerado (apenas texto)

### Formato aplicado

- Narrativa contínua em linguagem natural
- Sem títulos, tópicos, listas, markdown, capítulos
- Sem números de aulas, referências bíblicas explícitas ou divisões “parte 1 / parte 2”
- Tom conversacional entre especialistas; raciocínio progressivo, aplicações práticas e reflexão final

### Arquivos gerados

| Código | Disciplina | Caminho | Caracteres | Palavras |
| :---: | :--- | :--- | ---: | ---: |
| 01 | Introdução a Teologia | `01 Básico em Teologia/01 Introdução a Teologia/AUDIO_OVERVIEW.md` | 5.136 | 817 |
| 02 | Métodos de Estudos Bíblicos | `01 Básico em Teologia/02 Métodos de Estudos Bíblicos/AUDIO_OVERVIEW.md` | 4.037 | 632 |
| 03 | Homilética | `01 Básico em Teologia/03 Homilética/AUDIO_OVERVIEW.md` | 4.201 | 651 |
| 04 | Arqueologia e Geografia 1 | `01 Básico em Teologia/04 Arqueologia e Geografia 1/AUDIO_OVERVIEW.md` | 4.567 | 705 |
| 05 | Arqueologia e Geografia 2 | `01 Básico em Teologia/05 Arqueologia e Geografia 2/AUDIO_OVERVIEW.md` | 4.285 | 653 |
| 06 | Pentateuco | `01 Básico em Teologia/06 Pentateuco/AUDIO_OVERVIEW.md` | 3.896 | 583 |
| 07 | Doutrinas Bíblicas do VT | `01 Básico em Teologia/07 Doutrinas Bíblicas do Velho Testamento/AUDIO_OVERVIEW.md` | 3.309 | 465 |
| 08 | Teologia do Novo Testamento | `01 Básico em Teologia/08 Teologia do Novo Testamento/AUDIO_OVERVIEW.md` | 3.471 | 524 |
| 09 | Livros Poéticos | `01 Básico em Teologia/09 Livros Poéticos/AUDIO_OVERVIEW.md` | 3.270 | 502 |
| 10 | Hermenêutica | `01 Básico em Teologia/10 Hermenêutica/AUDIO_OVERVIEW.md` | 3.580 | 523 |
| 11 | Os Evangelhos | `01 Básico em Teologia/11 Os Evangelhos/AUDIO_OVERVIEW.md` | 3.687 | 553 |
| 12 | Heresiologia | `01 Básico em Teologia/12 Heresiologia/AUDIO_OVERVIEW.md` | 3.272 | 456 |
| | **Total** | **12 arquivos** | **46.711** | **7.064** |

### Observações

- Disciplina 05: arquivo anterior (formato estruturado com tabelas) substituído pelo novo padrão narrativo.
- Estimativa ElevenLabs: ~3.900–4.700 caracteres por disciplina (~3–5 min de narração em português, conforme voz e velocidade).
- Commit não solicitado nesta etapa.

---

## 12 Heresiologia

**Data**: 2026-06-04  
**Professor**: não informado nas aulas  
**Instituição**: Instituto Teológico Renacer  
**Aulas analisadas**: 28 (Aula 01 a Aula 28)

### Escopo processado

- Introdução: Heresiologia, apologética, *haireses*, sutileza, herança importada, cinco critérios de identificação de seitas
- Catolicismo romano: paganização, papado, purgatório, marilatria, missa/transubstanciação, apócrifos, Pedro/Petra
- Espiritismo: Kardec, Fox 1848, reencarnação vs *anástasis*, necromancia (1Sm 28, Dt 18)
- Mormonismo, adventismo (Miller, Ellen White, 1844), Testemunhas de Jeová
- Nova Era, Ciência Cristã, evolucionismo, unicidade (Só Jesus)
- Islamismo (cinco pilares, Alcorão), moonismo, budismo, maçonaria (33 graus, incompatibilidade cristã)

### Artefatos gerados

| Arquivo | Localização |
| :--- | :--- |
| KB_MASTER.md | `01 Básico em Teologia/12 Heresiologia/` |
| DOUTRINAS.md | `01 Básico em Teologia/12 Heresiologia/` |
| DICIONARIO.md | `01 Básico em Teologia/12 Heresiologia/` |
| VERSICULOS.md | `01 Básico em Teologia/12 Heresiologia/` |
| INDICE_SEMANTICO.md | `01 Básico em Teologia/12 Heresiologia/` |

### Métricas

- **Conceitos extraídos (DICIONARIO.md)**: 80
- **Versículos catalogados (VERSICULOS.md)**: 54
- **Doutrinas mapeadas (DOUTRINAS.md)**: 15
- **Personagens catalogados (DICIONARIO.md)**: 22
- **Eventos históricos catalogados (DICIONARIO.md)**: 6
- **Temas semânticos (INDICE_SEMANTICO.md)**: 19

### Commit

- **Mensagem**: `feat: gerar base de conhecimento da disciplina Heresiologia`
- **Hash**: `1eea9a97792ce324ec713214101c63355272466a`

### Observações

- Fontes: exclusivamente as 28 transcrições Markdown da disciplina.
- Nome do professor não citado nas transcrições; instituição como Instituto Renacer (grafias variadas).
- Aula 20 inclui vídeo incorporado (Lobo Conservador) sobre origens do Islã.
- **Fase 1B do Curso Básico em Teologia concluída** (12/12 disciplinas).
- Nenhum artefato global foi gerado nesta etapa.

---

## 11 Os Evangelhos

**Data**: 2026-06-04  
**Professor**: Pastor Tiago Domínguez  
**Instituição**: Instituto Teológico Renacê  
**Aulas analisadas**: 25 (Aula 01 a Aula 25)

### Escopo processado

- Quatro períodos bíblicos; Evangelhos como período da manifestação (~46% do NT)
- Etimologia (*euangelion*), cronologia, autores, destinatários, origem oral/documental
- Sinóticos, quatro testemunhas, quatro ofícios (Rei, Servo, Filho do Homem, Filho de Deus)
- Mateus: publicano, cumprimento, Espírito Santo, Reino, parábolas, Evangelho da Igreja
- Marcos: João Marcos, Evangelho da Atuação, servo com autoridade, perseguição (Nero), Mc 14
- Lucas: grego/médico, cronologia, 8 parábolas exclusivas, Salvador e Senhor, expiação na cruz
- João: anti-gnosticismo, Verbo, Consolador, vida eterna, João 3:16, harmonia das conclusões

### Artefatos gerados

| Arquivo | Localização |
| :--- | :--- |
| KB_MASTER.md | `01 Básico em Teologia/11 Os Evangelhos/` |
| DOUTRINAS.md | `01 Básico em Teologia/11 Os Evangelhos/` |
| DICIONARIO.md | `01 Básico em Teologia/11 Os Evangelhos/` |
| VERSICULOS.md | `01 Básico em Teologia/11 Os Evangelhos/` |
| INDICE_SEMANTICO.md | `01 Básico em Teologia/11 Os Evangelhos/` |

### Métricas

- **Conceitos extraídos (DICIONARIO.md)**: 64
- **Versículos catalogados (VERSICULOS.md)**: 47
- **Doutrinas mapeadas (DOUTRINAS.md)**: 15
- **Personagens catalogados (DICIONARIO.md)**: 29
- **Eventos históricos catalogados (DICIONARIO.md)**: 23
- **Temas semânticos (INDICE_SEMANTICO.md)**: 19

### Commit

- **Mensagem**: `feat: gerar base de conhecimento da disciplina Os Evangelhos`
- **Hash**: `8f4d90c524762d166971a12d2197b0c3690caa5f`

### Observações

- Fontes: exclusivamente as 25 transcrições Markdown da disciplina.
- Professor identificado na Aula 01 como Pastor Tiago Domínguez (transcrição: "Tiago Domíngus").
- Aulas 13-25 não repetem nome do professor; instituição citada com grafias variadas (Renacê/Renacer).
- Nenhum artefato global foi gerado nesta etapa.

---

## 10 Hermenêutica

**Data**: 2026-06-04  
**Professor**: Pastor Carvalho Júnior  
**Instituição**: Renacer Instituto Teológico  
**Aulas analisadas**: 14 (Aula 01 a Aula 14)

### Escopo processado

- Visão panorâmica: hermenêutica, exegese, intenção autoral; modelo de Atos 8 (Filipe e o eunuco)
- Etimologia Hermes/Mercúrio; Jesus hermeneuta (Emaús, Mc 4:34 *epilysken*)
- Abismos: geográfico, cultural, linguístico, autoral, cronológico, gramatical, sobrenatural
- Cultura bíblica e distinção P/T (permanente/temporário) em mandamentos culturais
- Exegese gramatical; Calvino; inspiração verbal; Sl 23:5 (*panah*, *shemen*); Tito em Creta
- Axioma humano (livro humano) e axioma divino (livro de Deus); gêneros literários
- Inspiração verbal (*theopneustos*); inerrância dos autógrafos; unidade e harmonização
- Iluminação vs. nova revelação; restrições (homem natural, 1 Co 2:14)
- Contexto inicial, imediato, remoto, gramatical; hebraísmos; Pv 22:28
- Conclusão: Tiago 1 (sophia, poietai, akroatai); prática da Palavra

### Artefatos gerados

| Arquivo | Localização |
| :--- | :--- |
| KB_MASTER.md | `01 Básico em Teologia/10 Hermenêutica/` |
| DOUTRINAS.md | `01 Básico em Teologia/10 Hermenêutica/` |
| DICIONARIO.md | `01 Básico em Teologia/10 Hermenêutica/` |
| VERSICULOS.md | `01 Básico em Teologia/10 Hermenêutica/` |
| INDICE_SEMANTICO.md | `01 Básico em Teologia/10 Hermenêutica/` |

### Métricas

- **Conceitos extraídos (DICIONARIO.md)**: 65
- **Versículos catalogados (VERSICULOS.md)**: 27
- **Doutrinas mapeadas (DOUTRINAS.md)**: 14
- **Personagens catalogados (DICIONARIO.md)**: 36
- **Eventos históricos catalogados (DICIONARIO.md)**: 13
- **Temas semânticos (INDICE_SEMANTICO.md)**: 16

### Commit

- **Mensagem**: `feat: gerar base de conhecimento da disciplina Hermenêutica`
- **Hash**: `fe35ff316c6b72be35bd68b27d6b70a7ffbf4197`

### Observações

- Fontes: exclusivamente as 14 transcrições Markdown da disciplina.
- Professor identificado nas aulas como Pastor Carvalho Júnior (transcrição: "Carvalho", "Carvalho Junho").
- Nenhum artefato global foi gerado nesta etapa.

---

## 09 Livros Poéticos

**Data**: 2026-06-04  
**Professor**: Natã Maestrel  
**Instituição**: Curso de Teologia Básico (apostila citada nas aulas)  
**Aulas analisadas**: 12 (Aula 01 a Aula 12)

### Escopo processado

- Introdução aos cinco livros poéticos/sapienciais (Salmos, Jó, Provérbios, Eclesiastes, Cânticos)
- Poesia hebraica: paralelismo (sinônimo, antitético, sintético), hemistíquios, versos livres
- Interpretação poética: nem literal nem alegórica; tipologia cautelosa em Cantares
- Jó: sofrimento, adoração verdadeira, historicidade, Satanás, redentor/mediador em Cristo
- Por que o justo sofre: pecado original, providência (Rm 8), exemplos (José, Davi, Paulo)
- Salmos: miniatura da Bíblia (Lutero); cinco livros; Halel egípcico; ~93 citações no NT
- Provérbios: sabedoria prática; guardar o coração (Pv 4:23); Salomão e Ezequias
- Eclesiastes: vaidade; temor do Senhor (Ec 12:13); alegria do ser vs. estar
- Cantares: amor conjugal literal; casamento como projeto de Deus; Megillot

### Artefatos gerados

| Arquivo | Localização |
| :--- | :--- |
| KB_MASTER.md | `01 Básico em Teologia/09 Livros Poéticos/` |
| DOUTRINAS.md | `01 Básico em Teologia/09 Livros Poéticos/` |
| DICIONARIO.md | `01 Básico em Teologia/09 Livros Poéticos/` |
| VERSICULOS.md | `01 Básico em Teologia/09 Livros Poéticos/` |
| INDICE_SEMANTICO.md | `01 Básico em Teologia/09 Livros Poéticos/` |

### Métricas

- **Conceitos extraídos (DICIONARIO.md)**: 86
- **Versículos catalogados (VERSICULOS.md)**: 50
- **Doutrinas mapeadas (DOUTRINAS.md)**: 14
- **Personagens catalogados (DICIONARIO.md)**: 33
- **Eventos históricos catalogados (DICIONARIO.md)**: 16
- **Temas semânticos (INDICE_SEMANTICO.md)**: 14

### Commit

- **Mensagem**: `feat: gerar base de conhecimento da disciplina Livros Poéticos`
- **Hash**: `f1fe5034a50b6188c685c2cb7970cd89880be202`

### Observações

- Fontes: exclusivamente as 12 transcrições Markdown da disciplina.
- Professor identificado na Aula 01 como Natã Maestrel.
- Nenhum artefato global foi gerado nesta etapa.

---

## 08 Teologia do Novo Testamento

**Data**: 2026-06-04  
**Professor**: não informado nas aulas  
**Instituição**: Instituto Teológico Renacer  
**Aulas analisadas**: 14 (Aula 01 a Aula 14)

### Escopo processado

- Organização do NT: evangelhos, Atos, epístolas paulinas, pastorais, Hebreus, católicas, Apocalipse
- Novo testamento como nova aliança (Hebreus 9:15-17); Paulo escreveu antes dos evangelhos
- Quatro evangelhos e Ezequiel 1:10 (leão/Mateus, boi/Marcos, homem/Lucas, águia/João)
- Seis doutrinas principais: Deus, salvação, Cristo, Espírito Santo, anjos, homem
- Eclesiologia e escatologia; pedra angular = Cristo (não Pedro)
- Ensinos de Jesus centrados na fé; teologia de João (cristocêntrica)
- Teologia de Pedro, Paulo (graça), Hebreus (superioridade de Cristo)
- Teologia de Tiago (fé e obras) e Judas (apologética)
- Teologia do Apocalipse (sete igrejas, Cordeiro herdeiro do trono)

### Artefatos gerados

| Arquivo | Localização |
| :--- | :--- |
| KB_MASTER.md | `01 Básico em Teologia/08 Teologia do Novo Testamento/` |
| DOUTRINAS.md | `01 Básico em Teologia/08 Teologia do Novo Testamento/` |
| DICIONARIO.md | `01 Básico em Teologia/08 Teologia do Novo Testamento/` |
| VERSICULOS.md | `01 Básico em Teologia/08 Teologia do Novo Testamento/` |
| INDICE_SEMANTICO.md | `01 Básico em Teologia/08 Teologia do Novo Testamento/` |

### Métricas

- **Conceitos extraídos (DICIONARIO.md)**: 101
- **Versículos catalogados (VERSICULOS.md)**: 77
- **Doutrinas mapeadas (DOUTRINAS.md)**: 15
- **Personagens catalogados (DICIONARIO.md)**: 29
- **Eventos históricos catalogados (DICIONARIO.md)**: 12
- **Temas semânticos (INDICE_SEMANTICO.md)**: 15

### Commit

- **Mensagem**: `feat: gerar base de conhecimento da disciplina Teologia do Novo Testamento`
- **Hash**: `8847b9eb24e17e7e1e6c8130194f6bc9516e40a7`

### Observações

- Fontes: exclusivamente as 14 transcrições Markdown da disciplina.
- Nome do professor não citado nas transcrições.
- Nenhum artefato global foi gerado nesta etapa.

---

## 07 Doutrinas Bíblicas do Velho Testamento

**Data**: 2026-06-04  
**Professor**: Pastor Thiago Domingos  
**Instituição**: Instituto Teológico Renacer  
**Aulas analisadas**: 19 (Aula 01 a Aula 19)

### Escopo processado

- Definição de teologia e doutrina bíblica; regras de formulação; apostasia
- Dez doutrinas fundamentais e cinco divisões teológicas do VT
- Períodos históricos e dispensacionalismo (sete dispensações)
- Era pré-patriarcal, patriarcal, mosaica, pré-monárquica e monárquica
- Doutrina da criação (*exahemeron*, *bará*); refutação de Big Bang, panteísmo e evolucionismo
- Teontologia: personalidade e atributos de Deus
- Antropologia: tricotomia (corpo, alma, espírito); homem carnal vs. espiritual
- Hamartologia: queda, terminologia hebraica do pecado, propensão ao mal
- Soteriologia: arrependimento, conversão, graça, sangue, fé
- Justificação, regeneração e santificação; três meios de santificação
- Tipologia sacrificial (vestes de pele, levítico, Páscoa)

### Artefatos gerados

| Arquivo | Localização |
| :--- | :--- |
| KB_MASTER.md | `01 Básico em Teologia/07 Doutrinas Bíblicas do Velho Testamento/` |
| DOUTRINAS.md | `01 Básico em Teologia/07 Doutrinas Bíblicas do Velho Testamento/` |
| DICIONARIO.md | `01 Básico em Teologia/07 Doutrinas Bíblicas do Velho Testamento/` |
| VERSICULOS.md | `01 Básico em Teologia/07 Doutrinas Bíblicas do Velho Testamento/` |
| INDICE_SEMANTICO.md | `01 Básico em Teologia/07 Doutrinas Bíblicas do Velho Testamento/` |

### Métricas

- **Conceitos extraídos (DICIONARIO.md)**: 89
- **Versículos catalogados (VERSICULOS.md)**: 47
- **Doutrinas mapeadas (DOUTRINAS.md)**: 13
- **Temas semânticos (INDICE_SEMANTICO.md)**: 13

### Commit

- **Mensagem**: `feat: gerar base de conhecimento da disciplina Doutrinas Bíblicas do Velho Testamento`
- **Hash**: `a84ce454ebcfdadad3a724985fbffc8e75a24289`

### Observações

- Fontes: exclusivamente as 19 transcrições Markdown da disciplina.
- Professor identificado nas aulas como Pastor Thiago Domingos.
- Nenhum artefato global foi gerado nesta etapa.

---

## 06 Pentateuco

**Data**: 2026-06-04  
**Professor**: Pastor Carvalho Júnior  
**Instituição**: Instituto Renacer (Renacer Instituto Teológico)  
**Aulas analisadas**: 15 (Aula 01 a Aula 15)

### Escopo processado

- Terminologia e limites do Pentateuco (Pentateuchos, Torá, Lei de Moisés)
- Divisões alternativas (Hexateuco, Octateuco, Enneateuco, Tetrateuco)
- Estrutura material (rolos separados, Qumran, Codex)
- Conteúdo por livro (Gênesis, Êxodo, Levítico, Números, Deuteronômio)
- Autoria mosaica e crítica literária (Ibn Ezra, Espinoza, hipóteses JEDP)
- Visão panorâmica de Gênesis (duas partes: 1-11 e 12-50)
- Era patriarcal e leis pré-mosaicas (hospitalidade, mistura de raça, vingança)
- Êxodo (libertação, cânticos, coluna de nuvem/fogo)
- Levítico (korban, sacerdócio, Nadabe e Abiú)
- Números (murmuração, setenta anciãos)
- Deuteronômio (discursos, aliança, Salmo 91)

### Artefatos gerados

| Arquivo | Localização |
| :--- | :--- |
| KB_MASTER.md | `01 Básico em Teologia/06 Pentateuco/` |
| DOUTRINAS.md | `01 Básico em Teologia/06 Pentateuco/` |
| DICIONARIO.md | `01 Básico em Teologia/06 Pentateuco/` |
| VERSICULOS.md | `01 Básico em Teologia/06 Pentateuco/` |
| INDICE_SEMANTICO.md | `01 Básico em Teologia/06 Pentateuco/` |

### Métricas

- **Conceitos extraídos (DICIONARIO.md)**: 75
- **Versículos catalogados (VERSICULOS.md)**: 37
- **Doutrinas mapeadas (DOUTRINAS.md)**: 12
- **Temas semânticos (INDICE_SEMANTICO.md)**: 13

### Commit

- **Mensagem**: `feat: gerar base de conhecimento da disciplina Pentateuco`
- **Hash**: `538a11f6557509216594e9db5ed769929311d5cd`

### Observações

- Fontes: exclusivamente as 15 transcrições Markdown da disciplina.
- Professor identificado nas aulas como Pastor Carvalho Júnior (transcrição: "Carvalho Junho").
- Nenhum artefato global foi gerado nesta etapa.

---

## Histórico anterior

| Disciplina | Commit |
| :--- | :--- |
| 01 Introdução a Teologia | a76bae8 |
| 02 Métodos de Estudos Bíblicos | a76bae8 |
| 03 Homilética | 6476311 |
| 04 Arqueologia e Geografia 1 | 0572fda |
| 05 Arqueologia e Geografia 2 | a76bae8 |
| 09 Livros Poéticos | f1fe503 |
| 10 Hermenêutica | fe35ff3 |
| 11 Os Evangelhos | 8f4d90c |
| 12 Heresiologia | 1eea9a9 |
