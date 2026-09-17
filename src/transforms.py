import pandas as pd

ptax = pd.read_json(r'C:\Users\imercado2\OneDrive - GIRANDO COMERCIO DE PECAS LTDA\iMercado - Eder Iago\ProjAPI\data\RAW\BCB\CAMBIO\ptax_USD.json')

dbgg13761 = pd.read_json(r'C:\Users\imercado2\OneDrive - GIRANDO COMERCIO DE PECAS LTDA\iMercado - Eder Iago\ProjAPI\data\RAW\BCB\DIVIDA_PUBLICA\dbgg_serie13761.json')

dbgg13762 = pd.read_json(r'C:\Users\imercado2\OneDrive - GIRANDO COMERCIO DE PECAS LTDA\iMercado - Eder Iago\ProjAPI\data\RAW\BCB\DIVIDA_PUBLICA\dbgg_serie13762.json')

dlsp4478 = pd.read_json(r'C:\Users\imercado2\OneDrive - GIRANDO COMERCIO DE PECAS LTDA\iMercado - Eder Iago\ProjAPI\data\RAW\BCB\DIVIDA_PUBLICA\dlsp_serie4478.json')

dlsp4513 = pd.read_json(r'C:\Users\imercado2\OneDrive - GIRANDO COMERCIO DE PECAS LTDA\iMercado - Eder Iago\ProjAPI\data\RAW\BCB\DIVIDA_PUBLICA\dlsp_serie4513.json')

selic11 = pd.read_json(r'C:\Users\imercado2\OneDrive - GIRANDO COMERCIO DE PECAS LTDA\iMercado - Eder Iago\ProjAPI\data\RAW\BCB\SELIC\selic_serie11.json')

selic1178 = pd.read_json(r'C:\Users\imercado2\OneDrive - GIRANDO COMERCIO DE PECAS LTDA\iMercado - Eder Iago\ProjAPI\data\RAW\BCB\SELIC\selic_serie1178.json')

selic432 = pd.read_json(r'C:\Users\imercado2\OneDrive - GIRANDO COMERCIO DE PECAS LTDA\iMercado - Eder Iago\ProjAPI\data\RAW\BCB\SELIC\selic_serie432.json')

selic4189 = pd.read_json(r'C:\Users\imercado2\OneDrive - GIRANDO COMERCIO DE PECAS LTDA\iMercado - Eder Iago\ProjAPI\data\RAW\BCB\SELIC\selic_serie4189.json')

selic4390 = pd.read_json(r'C:\Users\imercado2\OneDrive - GIRANDO COMERCIO DE PECAS LTDA\iMercado - Eder Iago\ProjAPI\data\RAW\BCB\SELIC\selic_serie4390.json')

ipca655 = pd.read_json(r'C:\Users\imercado2\OneDrive - GIRANDO COMERCIO DE PECAS LTDA\iMercado - Eder Iago\ProjAPI\data\RAW\IBGE\IPCA\ipca655.json')

serie = ipca655.loc[0,"resultados"][0]["series"][0]["serie"]

ipca655_63 = []

for periodo, valor in serie.items():
    ipca655_63.append({"periodo":periodo,"valor":valor})

ipca655_final = pd.DataFrame(ipca655_63)

ipca1419 = pd.read_json(r'C:\Users\imercado2\OneDrive - GIRANDO COMERCIO DE PECAS LTDA\iMercado - Eder Iago\ProjAPI\data\RAW\IBGE\IPCA\ipca1419.json')


ipca1419_63 = ipca1419.loc[ipca1419['id'] == 63, 'resultados'].iloc[0]

ipca1419_63_final = ipca1419_63[0]['series'][0]['serie']




#print(ipca655_final)

#print(ipca1419.columns)
#print(ipca1419.head())
print(ipca1419_63_final)
#print(ipca655)
#resultado = ipca655.loc[0, "resultados"]
#print(type(resultado))