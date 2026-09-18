import pandas as pd
from functions import extrair_json, tipos_coluna, salvar_parquet
from pathlib import Path
from functools import reduce

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT/'data'
RAW = DATA/'RAW'
BCB = RAW/'BCB'
IBGE = RAW/'IBGE'
CAMBIO = BCB/'CAMBIO'
DIVIDA = BCB/'DIVIDA_PUBLICA'
SELIC = BCB/'SELIC'
IPCA = IBGE/'IPCA'

# na main - ptax = tratar_ptax(ptax_USD)
def tratar_ptax(arquivo):
    
    ptax = pd.read_json(CAMBIO/f'{arquivo}.json')
    
    ptax['dataHoraCotacao'] = pd.to_datetime(ptax['dataHoraCotacao'])
    
    ptax['data'] = ptax['dataHoraCotacao'].dt.date
    
    ptax = ptax.reindex(columns=['data', 'cotacaoCompra', 'cotacaoVenda'])

    ptax = ptax.astype({'data':'datetime64[us]', 'cotacaoCompra':'float64', 'cotacaoVenda':'float64'})

    return ptax

# na main tratar_divida('dbgg_serie13761', 'dbgg_serie13762')
def tratar_divida(arquivo1, arquivo2):
    
    divida1 = pd.read_json(DIVIDA/f'{arquivo1}.json')

    divida2 = pd.read_json(DIVIDA/f'{arquivo2}.json')
    
    divida = pd.merge(divida1, divida2, on='data', how='inner')
    
    divida.rename(columns={'valor_x':'divida_RS', 'valor_y':'divida_%PIB'}, inplace=True)
    
    divida['data'] = pd.to_datetime(divida['data'])
    
    return divida

# na main tratar_selic_diaria('selic_serie11','selic_serie1178','selic_serie432')
def tratar_selic_diaria(arquivo1, arquivo2, arquivo3):
    
    arquivo1 = pd.read_json(SELIC/f'{arquivo1}.json')
    arquivo2 = pd.read_json(SELIC/f'{arquivo2}.json')
    arquivo3 = pd.read_json(SELIC/f'{arquivo3}.json')
    
    lista_arquivo = [arquivo1, arquivo2, arquivo3]
    
    selic = reduce(lambda left, right: pd.merge(left, right, on='data', how='inner'), lista_arquivo)
    
    selic.rename(columns={
        'valor_x':'selic_efetiva',
        'valor_y':'selic_anualizada',
        'valor':'meta_selic'
    }, inplace=True)
    
    selic['data'] = pd.to_datetime(selic['data'], dayfirst=True)
    
    return selic

# na main tratar_selic_mensal('selic_serie4189','selic_serie4390')
def tratar_selic_mensal(arquivo1, arquivo2):
    
    arquivo1 = pd.read_json(SELIC/f'{arquivo1}.json')
    arquivo2 = pd.read_json(SELIC/f'{arquivo2}.json')
    
    selic = pd.merge(arquivo1,arquivo2, on='data', how='inner')
    
    selic.rename(columns={'valor_x':'acum_anualizada', 'valor_y':'acum_mensal'})
    
    selic['data'] = pd.to_datetime(selic['data'], dayfirst=True)
    
    return selic  
   
lista_ipca = 'ipca1419','ipca2938','ipca7060','ipca655'

def tratar_ipca(lista_df):
    
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



    
   
    
    