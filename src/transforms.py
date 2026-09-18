import pandas as pd
from functions import extrair_json, tipos_coluna, salvar_parquet
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT/'data'
RAW = DATA/'RAW'
BCB = RAW/'BCB'
IBGE = RAW/'IBGE'
CAMBIO = BCB/'CAMBIO'
DIVIDA = BCB/'DIVIDA_PUBLICA'
SELIC = BCB/'SELIC'
IPCA = IBGE/'IPCA'

ptax = pd.read_json(CAMBIO/'ptax_USD.json')

dbgg13761 = pd.read_json(DIVIDA/'dbgg_serie13761.json')

dbgg13762 = pd.read_json(DIVIDA/'dbgg_serie13762.json')

dlsp4478 = pd.read_json(DIVIDA/'dlsp_serie4478.json')

dlsp4513 = pd.read_json(DIVIDA/'dlsp_serie4513.json')

selic11 = pd.read_json(SELIC/'selic_serie11.json')

selic1178 = pd.read_json(SELIC/'selic_serie1178.json')

selic432 = pd.read_json(SELIC/'selic_serie432.json')

selic4189 = pd.read_json(SELIC/'selic_serie4189.json')

selic4390 = pd.read_json(SELIC/'selic_serie4390.json')

ipca655 = pd.read_json(IPCA/'ipca655.json')

ipca1419 = pd.read_json(IPCA/'ipca1419.json')

ipca2938 = pd.read_json(IPCA/'ipca2938.json')

ipca7060 = pd.read_json(IPCA/'ipca7060.json')

ipca655_63 = pd.DataFrame(extrair_json(ipca655,63))

ipca1419_63 = pd.DataFrame(extrair_json(ipca1419,63))

ipca1419_69 = pd.DataFrame(extrair_json(ipca1419,69))

ipca2938_63 = pd.DataFrame(extrair_json(ipca2938,63))

ipca2938_69 = pd.DataFrame(extrair_json(ipca2938,69))

ipca7060_63 = pd.DataFrame(extrair_json(ipca7060,63))

ipca7060_69 = pd.DataFrame(extrair_json(ipca7060,69))

ptax['dataHoraCotacao'] = pd.to_datetime(ptax['dataHoraCotacao'])

ptax['data'] = ptax['dataHoraCotacao'].dt.date

ptax.drop(columns=['dataHoraCotacao'], inplace=True)

ptax = ptax.reindex(columns=['data', 'cotacaoCompra', 'cotacaoVenda'])

ptax = ptax.astype({'data':'datetime64[us]', 'cotacaoCompra':'float64', 'cotacaoVenda':'float64'})

lista_ipca = [ipca655_63, ipca1419_63, ipca1419_69, ipca2938_63, ipca2938_69, ipca7060_63, ipca7060_69]

for df in lista_ipca:
    df.rename(columns={'periodo':'data'}, inplace=True)
    df['data'] = pd.to_datetime(df['data'], format="%Y%m")

dbgg13761 = tipos_coluna(dbgg13761)

dbgg13762 = tipos_coluna(dbgg13762)

dlsp4513 = tipos_coluna(dlsp4513)

dlsp4478 = tipos_coluna(dlsp4478)

selic11 = tipos_coluna(selic11)

selic1178 = tipos_coluna(selic1178)

selic432 = tipos_coluna(selic432)

selic4189 = tipos_coluna(selic4189)

selic4390 = tipos_coluna(selic4390)

salvar_parquet('BCB/CAMBIO', 'ptax', ptax)

salvar_parquet('BCB/DIVIDA', 'dbgg13761', dbgg13761)

salvar_parquet('BCB/DIVIDA', 'dbgg13762', dbgg13762)

salvar_parquet('BCB/DIVIDA', 'dlsp4513', dlsp4513)

salvar_parquet('BCB/DIVIDA', 'dlsp4478', dlsp4478)

salvar_parquet('BCB/SELIC','selic11', selic11)

salvar_parquet('BCB/SELIC','selic1178', selic1178)

salvar_parquet('BCB/SELIC','selic432', selic432)

salvar_parquet('BCB/SELIC','selic4189', selic4189)

salvar_parquet('BCB/SELIC','selic4390', selic4390)

salvar_parquet('IBGE/IPCA','ipca655_63', ipca655_63)

salvar_parquet('IBGE/IPCA','ipca1419_63', ipca1419_63)

salvar_parquet('IBGE/IPCA','ipca1419_69', ipca1419_69)

salvar_parquet('IBGE/IPCA','ipca2938_63', ipca2938_63)

salvar_parquet('IBGE/IPCA','ipca2938_69', ipca2938_69)

salvar_parquet('IBGE/IPCA','ipca7060_63', ipca7060_63)

salvar_parquet('IBGE/IPCA','ipca7060_69', ipca7060_69)





  

    






