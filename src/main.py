from datetime import date
from functions import salvar_json
from request_bcb import buscar_serie_diaria, buscar_serie_mensal, buscar_serie_cambio
from request_ibge import buscar_dados_ibge

# Requests SELIC - BCB/SGS

# Request Serie 11 - Selic Efetiva Diaria
serie11 = buscar_serie_diaria(11,date(2000,1,1), date(2026,8,31))
salvar_json('BCB/SELIC', 'selic_serie11', serie11)

# Request Serie 1178 - Selic Efetiva Diaria Anualizada
serie1178 = buscar_serie_diaria(1178,date(2000,1,1), date(2026,8,31))
salvar_json('BCB/SELIC', 'selic_serie1178', serie1178)

# Request Serie 4189 - Selic acumulada mês Anualizada
serie4189 = buscar_serie_mensal(4189,date(2000,1,1), date(2026,8,31))
salvar_json('BCB/SELIC', 'selic_serie4189', serie4189)

# Request Serie 432 - Meta Selic
serie432 = buscar_serie_mensal(432,date(2000,1,1), date(2026,8,31))
salvar_json('BCB/SELIC', 'selic_serie432', serie432)

# Request Serie 4390 - Selic acumulada mês
serie4390 = buscar_serie_mensal(4390,date(2000,1,1), date(2026,8,31))
salvar_json('BCB/SELIC', 'selic_serie4390', serie4390)

# Requests IPCA - IBGE

# Request Tabela 7060 - IPCA
ipca7060 = buscar_dados_ibge(7060, date(2020,1,1), date(2020,12,1), ['69','63'], "N1[all]", "315[7169]")
salvar_json('IBGE/IPCA', 'ipca7060', ipca7060)

# Request Tabela 2938 - IPCA
ipca2938 = buscar_dados_ibge(2938, date(2006,7,1), date(2011,12,1), ['69','63'], "N1[all]", "315[7169]")
salvar_json('IBGE/IPCA','ipca2938', ipca2938)

# Request Tabela 1419 - IPCA
ipca1419 = buscar_dados_ibge(1419, date(2012,1,1), date(2019,12,1), ['69','63'], "N1[all]", "315[7169]")
salvar_json('IBGE/IPCA','ipca1419', ipca1419)

# Request Tabela 655 - IPCA
ipca655 = buscar_dados_ibge(655, date(2000,1,1), date(2006,6,1), ['63'], "N1[all]", "315[7169]")
salvar_json('IBGE/IPCA','ipca655', ipca655)

# Requests DLSP - BCB/SGS

# Request Serie 4513 - DLSP (% do PIB)
serie4513 = buscar_serie_mensal(4513,date(2001,12,1), date(2026,7,31))
salvar_json('BCB/DIVIDA_PUBLICA','dlsp_serie4513', serie4513)

# Request Serie 4478 - DLSP (em milhões R$)
serie4478= buscar_serie_mensal(4478,date(2001,12,1), date(2026,7,31))
salvar_json('BCB/DIVIDA_PUBLICA','dlsp_serie4478', serie4478)

# Requests DBGG - BCB/SGS

# Request Serie 13762 - DBGG (% do PIB)
serie13762 = buscar_serie_mensal(13762,date(2006,12,1), date(2026,7,31))
salvar_json('BCB/DIVIDA_PUBLICA','dbgg_serie13762', serie13762)

# Request Serie 13761 - DBGG (em milhões R$)
serie13761 = buscar_serie_mensal(13761,date(2006,12,1), date(2026,7,31))
salvar_json('BCB/DIVIDA_PUBLICA','dbgg_serie13761', serie13761)

# Requests Cambio/USD - BCB/PTAX

# Requets Cotacao Dolar Periodo
serie_USD = buscar_serie_cambio('01-03-2000', '31-08-2026')
salvar_json('BCB/CAMBIO', 'ptax_USD', serie_USD)

