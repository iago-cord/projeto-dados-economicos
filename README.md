# Pipeline de Dados Econômicos

Projeto de estudo e portfólio voltado a coleta, armazenamento e análise de indicaores econômicos brasileiros.

O projeto utiliza dados públicos disponibilizados pelo Banco Central do Brasil(BCB) através da API SGS.

## Objetivo

Construir de forma incremental, um pipeline de dados econômicos capaz de:

- Coletar dados historicos através de APIs públicas;
- Implementar tratamento de erros e novas tentativas de requisição;
- Registrar execução através de logs;
- Armazenar os dados coletados;
- Persistir os dados em PostgreSQL;
- Realizar cargas incrementais;
- Automatizar a execução do pipeline;
- Aplicar transformações e análises estatísticas/econométricas.

## Tecnologias

- Python
- Requests
- Pandas
- PostgreSQL
- SQLAlchemy
- Power BI
- Airflow
- Git/Github

## Fonte dos dados

Os dados utilizados inicialmente são provenientes do Sistema Gerenciador de Série Temporais (SGS) do Banco Central do Brasil.

### Séries utilizadas

Série 11 - Selic efetiva diária
Série 1178 - Selic efetiva diária Anualizada / Base 252
Série 4189 - Selic acumulada mês Anualizada / Base 252
Série 432 - Meta Selic
Série 4390 - Selic acumulada mês

## Estrutura do Projeto

projeto-dados-economicos/
    data/
    logs/
    src/
        functions.py
        request_bcb.py
    
    .gitignore
    README.me
    requirements.txt

## Coleta

A coleta histórica é realizada em períodos menores para evitar limitações da API.

O pipeline possui:

- Tratamento de erros HTTP;
- retry para erros temporários;
- exponential backoff;
- validação da resposta;
- registro das etapas da execução através de logs.

## Status do projeto

### Concluido

[x] Coleta de dados através da API do BCB
[x] Coleta Histórica
[x] Divisão das requisições em períodos
[x] Retry de requisições
[x] Exponential backoff
[x] Logging
[x] Armazenamento dos dados em JSON

### Proximas etapas

[ ] PostgreSQL
[ ] SQLAlchemy
[ ] Carga incremental
[ ] Upsert dos dados
[ ] Airflow
[ ] Transformações dos dados
[ ] Analises estatísticas e econométricas
[ ] Dashboard no Power BI




