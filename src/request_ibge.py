import logging
import logger
from pathlib import Path
from functions import gerar_periodos_ibge, retry_request

ROOT = Path(__file__).resolve().parent.parent
LOGS = ROOT/"logs"
DATA = ROOT/"data"
LOGS.mkdir(exist_ok=True)
DATA.mkdir(exist_ok=True)

logger = logging.getLogger(__name__)

def buscar_dados_ibge(tabela, dt_inicio, dt_final,variavel, localidade, classificacao):
    
    periodos = gerar_periodos_ibge(dt_inicio,dt_final)
    
    variaveis = "|".join(variavel)
    
    url_ibge = f'https://servicodados.ibge.gov.br/api/v3/agregados/{tabela}/periodos/{periodos}/variaveis/{variaveis}'
    
    params = {
        "localidades": localidade,
        "classificacao": classificacao
    }
    
    try:
        logger.info(f"Tabela {tabela} | Coletando Periodo {dt_inicio} até {dt_final}")
        dados = retry_request(url_ibge, params=params,contexto=f"Tabela {tabela} | {dt_inicio} até {dt_final}")
        
    except RuntimeError as erro:
        raise RuntimeError(
            f"Erro ao buscar Tabela {tabela} "
            f"no periodo {dt_inicio} até {dt_final}: {erro}"
        ) from erro
        
    total = sum(
        len(s["serie"])
        for var in dados
        for res in var.get("resultados", [])
        for s in res.get("series", [])
    )
        
    logger.info(f"Tabela {tabela} | Coleta concluida | Total: {total} registros")
    return dados