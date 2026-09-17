# Pipeline de Dados Econômicos

Projeto de estudo e portfólio voltado à **coleta, organização, armazenamento e análise de dados econômicos brasileiros**, utilizando dados públicos disponibilizados por instituições como o **Banco Central do Brasil (BCB)** e o **Instituto Brasileiro de Geografia e Estatística (IBGE)**.

O projeto está sendo desenvolvido de forma incremental, evoluindo de uma etapa inicial de coleta de dados através de APIs públicas para uma arquitetura completa de **pipeline de dados**, com armazenamento em camada RAW, metadados, transformação, persistência em PostgreSQL, cargas incrementais e posterior automação do processo.

---

## Objetivo

Construir um pipeline de dados econômicos capaz de:

* Coletar dados históricos através de APIs públicas;
* Organizar os dados coletados em uma camada RAW;
* Preservar os dados originais das fontes;
* Documentar as séries através de metadados;
* Implementar tratamento de erros e novas tentativas de requisição;
* Registrar a execução do pipeline através de logs;
* Transformar e padronizar os dados;
* Persistir os dados em PostgreSQL;
* Implementar cargas incrementais;
* Utilizar operações de upsert para atualização dos dados;
* Automatizar a execução do pipeline;
* Construir análises estatísticas e econométricas;
* Disponibilizar os dados para ferramentas de BI;
* Explorar posteriormente aplicações de Data Science sobre séries econômicas.

---

## Arquitetura

A arquitetura planejada para o projeto segue o fluxo:

```text
                    APIs Públicas
                         │
              ┌──────────┴──────────┐
              │                     │
             BCB                   IBGE
              │                     │
              └──────────┬──────────┘
                         ↓
                    Coleta Python
                         ↓
                  Camada RAW JSON
                         ↓
                    Metadata
                         ↓
                  Transformações
                         ↓
                 PostgreSQL / Neon
                         ↓
                  Cargas incrementais
                         ↓
                     Airflow
                         ↓
              ┌──────────┴──────────┐
              │                     │
            Power BI         Análises / DS
```

A camada RAW tem como objetivo preservar os dados obtidos diretamente das APIs, mantendo uma cópia dos dados de origem antes das transformações.

---

## Fontes de dados

### Banco Central do Brasil

O projeto utiliza diferentes serviços e séries disponibilizados pelo Banco Central do Brasil.

#### Sistema Gerenciador de Séries Temporais — SGS

Inicialmente foram utilizadas séries relacionadas à taxa Selic e à dívida pública.

**Selic**

| Série | Indicador                                    |
| ----: | -------------------------------------------- |
|    11 | Selic efetiva diária                         |
|  1178 | Selic efetiva diária anualizada — Base 252   |
|  4189 | Selic acumulada no mês anualizada — Base 252 |
|   432 | Meta Selic                                   |
|  4390 | Selic acumulada no mês                       |

**Dívida pública**

| Série | Indicador                              |
| ----: | -------------------------------------- |
|  4478 | Dívida Líquida do Setor Público — DLSP |
|  4513 | DLSP em relação ao PIB                 |
| 13761 | Dívida Bruta do Governo Geral — DBGG   |
| 13762 | DBGG em relação ao PIB                 |

#### PTAX

Também são coletadas informações de câmbio através da API PTAX do Banco Central.

Atualmente o projeto utiliza a cotação do dólar americano em relação ao real.

---

### Instituto Brasileiro de Geografia e Estatística — IBGE

O projeto também utiliza dados do sistema SIDRA para obtenção do **IPCA**.

Foram utilizadas diferentes tabelas do IBGE para cobrir períodos históricos distintos da série:

| Tabela | Período    |
| -----: | ---------- |
|    655 | 1999–2006  |
|   2938 | 2006–2011  |
|   1419 | 2012–2019  |
|   7060 | 2020–atual |

Essa divisão permite construir uma série histórica mais extensa utilizando as diferentes tabelas disponibilizadas pelo IBGE ao longo do tempo.

---

## Coleta de dados

A coleta é realizada utilizando Python e requisições HTTP através da biblioteca `Requests`.

Para reduzir problemas relacionados a limites ou instabilidades das APIs, as consultas históricas são divididas em períodos menores.

O processo possui:

* Tratamento de erros HTTP;
* Retry de requisições;
* Exponential backoff;
* Timeout das requisições;
* Validação das respostas;
* Logging das etapas da execução;
* Organização dos dados por fonte e indicador.

As funções de coleta são separadas por fonte, enquanto funções genéricas de infraestrutura são mantidas em módulos reutilizáveis.

---

## Camada RAW

Os dados obtidos das APIs são armazenados inicialmente em formato JSON, preservando o conteúdo retornado pelas fontes.

Estrutura atual:

```text
data/
├── RAW/
│   ├── BCB/
│   │   ├── CAMBIO/
│   │   ├── DIVIDA_PUBLICA/
│   │   └── SELIC/
│   │
│   └── IBGE/
│       └── IPCA/
│
└── metadata/
    ├── BCB/
    └── IBGE/
```

A separação entre dados RAW e dados transformados permite manter a rastreabilidade do processo e possibilita a reconstrução das etapas posteriores do pipeline.

---

## Metadata

Além dos dados propriamente ditos, o projeto mantém arquivos de metadados descrevendo as séries utilizadas.

Entre as informações documentadas estão:

* Fonte;
* Sistema/API;
* Código da série;
* Nome do indicador;
* Descrição;
* Unidade de medida;
* Periodicidade;
* Período histórico;
* Período coletado;
* Endpoint utilizado;
* Categoria do indicador.

A intenção é manter separadas as informações **sobre os dados** dos próprios dados coletados.

---

## Tecnologias

* Python
* Requests
* Pandas
* PostgreSQL
* SQLAlchemy
* Power BI
* Apache Airflow
* Git
* GitHub

---

## Estrutura do projeto

```text
projeto-dados-economicos/
│
├── data/
│   ├── RAW/
│   │   ├── BCB/
│   │   │   ├── CAMBIO/
│   │   │   ├── DIVIDA_PUBLICA/
│   │   │   └── SELIC/
│   │   │
│   │   └── IBGE/
│   │       └── IPCA/
│   │
│   └── metadata/
│       ├── BCB/
│       └── IBGE/
│
├── logs/
│
├── src/
│   ├── functions.py
│   ├── main.py
│   ├── request_bcb.py
│   └── request_ibge.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

---

## Status do projeto

### Concluído

* [x] Estrutura inicial do projeto
* [x] Integração com APIs públicas
* [x] Coleta histórica
* [x] Coleta BCB — SGS
* [x] Coleta BCB — PTAX
* [x] Coleta IBGE — SIDRA
* [x] Divisão das requisições em períodos
* [x] Tratamento de erros HTTP
* [x] Retry de requisições
* [x] Exponential backoff
* [x] Timeout das requisições
* [x] Validação das respostas
* [x] Logging
* [x] Armazenamento dos dados em JSON
* [x] Organização da camada RAW
* [x] Estrutura inicial de metadados

### Em desenvolvimento

* [ ] Padronização e transformação dos dados
* [ ] Modelagem do banco de dados
* [ ] PostgreSQL
* [ ] SQLAlchemy
* [ ] Carga inicial
* [ ] Cargas incrementais
* [ ] Upsert dos dados
* [ ] Validação da camada de dados
* [ ] Automação do pipeline com Airflow
* [ ] Monitoramento das execuções
* [ ] Documentação da arquitetura

### Próximas etapas

* [ ] Construção das tabelas analíticas
* [ ] Análise exploratória dos indicadores
* [ ] Análises estatísticas
* [ ] Análises de séries temporais
* [ ] Análises econométricas
* [ ] Dashboard no Power BI
* [ ] Aplicações de Data Science / Machine Learning

---

## Evolução planejada

O projeto está sendo desenvolvido em etapas, começando pela construção da infraestrutura de coleta e armazenamento e evoluindo posteriormente para análise.

```text
Coleta
  ↓
RAW
  ↓
Metadata
  ↓
Transformação
  ↓
PostgreSQL
  ↓
Carga incremental
  ↓
Automação
  ↓
Análise
  ↓
BI / Data Science
```

A ideia é que o projeto evolua de uma simples coleta de dados públicos para uma pequena plataforma de dados econômicos, permitindo trabalhar com séries históricas e construir análises reproduzíveis a partir dos dados coletados.



