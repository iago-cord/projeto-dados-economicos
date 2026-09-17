import requests
import pandas as pd
import json
from datetime import date
from src.request_bcb import buscar_serie_mensal, buscar_serie_diaria
from src.functions import retry_request


#url_servidores = 'https://api.portaldatransparencia.gov.br/api-de-dados/servidores'

#url_siape = 'https://servicodados.ibge.gov.br/api/v3/agregados'

#url_servidores = 'https://api.portaldatransparencia.gov.br/api-de-dados/servidores/renuncias-valor'

#salvar_json('serie4513', serie4513)

url = "https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoMoedaPeriodoFechamento(codigoMoeda=@codigoMoeda,dataInicialCotacao=@dataInicialCotacao,dataFinalCotacao=@dataFinalCotacao)"

params = {
    "@codigoMoeda":"'USD'",
    "@dataInicialCotacao":"'01-02-2025'",
    "@dataFinalCotacao":"'01-02-2025'",
    "$format":"json"
}

headers = {
    "Accept":"application/json"
}

response = requests.get(url, params=params, headers=headers)

response.raise_for_status()

dados = response.json()

print(dados)

'''
tabela = 7060

periodos = '202001|202002|202101'

variavel = '69|2265'

url_ibge = f'https://servicodados.ibge.gov.br/api/v3/agregados/{tabela}/periodos/{periodos}/variaveis/{variavel}'

params = {
    "localidades": "N1[all]",
    "classificacao": "315[7169]"
}

response = requests.get(url_ibge, params=params)

dados = response.json()

with open('ipca.json', 'w', encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)

print(dados)
print(response.status_code)
print(response.url)


'''