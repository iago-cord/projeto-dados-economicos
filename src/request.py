import requests
import pandas as pd
import json
from datetime import date
from request_bcb import buscar_serie_mensal, buscar_serie_diaria
from functions import retry_request, tipos_coluna, extrair_json
from pathlib import Path
from functools import reduce
import itertools

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT/'data'
RAW = DATA/'RAW'
BCB = RAW/'BCB'
IBGE = RAW/'IBGE'
CAMBIO = BCB/'CAMBIO'
DIVIDA = BCB/'DIVIDA_PUBLICA'
SELIC = BCB/'SELIC'
IPCA = IBGE/'IPCA'

#dbgg13761 = pd.read_json(DIVIDA/'dbgg_serie13761.json')

#dbgg13762 = pd.read_json(DIVIDA/'dbgg_serie13762.json')

lista_ipca = 'ipca1419','ipca2938','ipca7060','ipca655'

def ipca(lista_df):
    
    lista_arquivos = []
    
    for df in lista_df:
        arquivo = pd.read_json(IPCA/f'{df}.json')
        
        lista_arquivos.append(arquivo)
        
    dados_63 = []
    dados_69 = []
        
    for i in range(len(lista_arquivos)):
            
        dados63 = pd.DataFrame(extrair_json(lista_arquivos[i],63))
        dados_63.append(dados63)
        try:
            dados69 = pd.DataFrame(extrair_json(lista_arquivos[i],69))
            dados_69.append(dados69)
        except:
            pass
        
    ipca69 = pd.concat(dados_69, ignore_index=True)
    ipca63 = pd.concat(dados_63,ignore_index=True)
    
    ipca = pd.merge(ipca63, ipca69, on='periodo', how='left')
    
    ipca.rename(columns={
            'periodo':'data',
            'valor_x':'var_mensal',
            'valor_y':'acum_12_meses'
        }, inplace=True)
        
    ipca['data'] = pd.to_datetime(ipca['data'], format='%Y%m')
    
    ipca = ipca.sort_values(by='data', ascending=True)
                
    return ipca
    
    

teste = ipca(lista_ipca)

print(teste)

'''

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