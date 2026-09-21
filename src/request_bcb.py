from datetime import date, timedelta
from dateutil.relativedelta import relativedelta
import logging
import logger
from pathlib import Path
from functions import retry_request

ROOT = Path(__file__).resolve().parent.parent
LOGS = ROOT/"logs"
DATA = ROOT/"data"
LOGS.mkdir(exist_ok=True)
DATA.mkdir(exist_ok=True)

logger = logging.getLogger(__name__)

def buscar_serie_diaria(serie, dt_inicio, dt_final):
    
    max_intervalo = 10
    
    resultado = []
    
    while dt_inicio <= dt_final :
    
        fim = date(dt_inicio.year + (max_intervalo -1 ), dt_inicio.month, dt_inicio.day)
        
        if fim > dt_final: fim = dt_final
        
        url = (
            f'https://api.bcb.gov.br/dados/serie/bcdata.sgs.{serie}/dados'
        )
        
        params = {
            "formato": "json",
            "dataInicial": dt_inicio.strftime("%d/%m/%Y"),
            "dataFinal": fim.strftime("%d/%m/%Y")
        }
        
        try:
            logger.info(f"Série {serie} | Coletando Periodo {dt_inicio} até {fim}")
            dados = retry_request(url, params=params,contexto=f"Série {serie} | {dt_inicio} até {fim}")
            
            resultado.extend(dados)
            logger.info(f"Série {serie} | Periodo {dt_inicio} até {fim} concluido | {len(dados)} registros")
            
        except RuntimeError as erro:
            raise RuntimeError(
                f"Erro ao buscar série {serie} "
                f"no periodo {dt_inicio} até {fim}: {erro}"
            ) from erro
        
        dt_inicio = fim + timedelta(days=1)
        
    logger.info(f"Série {serie} | Coleta concluida | Total: {len(resultado)} registros")
    return resultado


def buscar_serie_mensal(serie, dt_inicio, dt_final):
    
    max_intervalo = 10
    
    resultado = []
    
    while dt_inicio <= dt_final :
    
        fim = date(dt_inicio.year + (max_intervalo -1 ), dt_inicio.month, dt_inicio.day)
        
        if fim > dt_final: fim = dt_final
        
        url = (
            f'https://api.bcb.gov.br/dados/serie/bcdata.sgs.{serie}/dados'
        )
        
        params = {
            "formato": "json",
            "dataInicial": dt_inicio.strftime("%d/%m/%Y"),
            "dataFinal": fim.strftime("%d/%m/%Y")
        }
        
        try:
            logger.info(f"Série {serie} | Coletando Periodo {dt_inicio} até {fim}")
            dados = retry_request(url, params=params,contexto=f"Série {serie} | {dt_inicio} até {fim}")
                    
            resultado.extend(dados)
            logger.info(f"Série {serie} | Periodo {dt_inicio} até {fim} concluido | {len(dados)} registros")
                    
        except RuntimeError as erro:
            raise RuntimeError(
                    f"Erro ao buscar série {serie} "
                    f"no periodo {dt_inicio} até {fim}: {erro}"
                    ) from erro
                
        dt_inicio = fim + relativedelta(months=1)
    
    logger.info(f"Série {serie} | Coleta concluida | Total: {len(resultado)} registros")
    return resultado

def buscar_serie_cambio(dt_inicio, dt_final):
    
    url_bcb_cambio = "https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarPeriodo(dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)"
        
    params = {
        #"@codigoMoeda":f"'{moeda}'",
        "@dataInicial":f"'{dt_inicio}'",
        "@dataFinalCotacao":f"'{dt_final}'",
        "$format":"json"
    }

    headers = {
    "Accept":"application/json"
    }

    try:
        logger.info(f"Moeda USD | Coletando Periodo {dt_inicio} até {dt_final}")
        dados = retry_request(url_bcb_cambio,params=params, headers=headers, contexto=f"Moeda USD | {dt_inicio} até {dt_final}")
        registros = dados.get("value",[])
    
    except RuntimeError as erro:
        raise RuntimeError(
            f"Erro ao buscar Moeda USD "
            f"no periodo {dt_inicio} até {dt_final}"
        )from erro
        
    logger.info(f"Moeda USD | Coleta Concluida | Total:{len(registros)}")
    return registros

