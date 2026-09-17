import requests
import json
from dateutil.relativedelta import relativedelta
import time
import logging
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LOGS = ROOT/"logs"
DATA = ROOT/"data"/"RAW"
LOGS.mkdir(exist_ok=True)
DATA.mkdir(exist_ok=True)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

file_handler = logging.FileHandler(LOGS / "pipeline_coleta.log", encoding="utf-8")

console_handler = logging.StreamHandler()

file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)

def retry_request(url, params, headers = None, tentativas=3, espera=2, contexto = None):
    
    for tentativa in range (1, tentativas + 1):
        
        try:
            logger.info(f"{contexto} | Iniciando Requisição")
            response = requests.get(url, params=params, headers=None, timeout=30)
            
            response.raise_for_status()
            
            data = response.json()
            
            if not data:
                raise RuntimeError(
                    f"A resposta da API esta vazia para o periodo "
                    f"{params['dataInicial']} ate {params['dataFinal']}"
                )
            else:
                logger.info(f"{contexto} | Requisição concluida | {len(data)} registros retornados")
                return data
            
        except requests.exceptions.RequestException as erro_temporario:
            
            erros = [429,500,502,503,504]
            
            status_code = (erro_temporario.response.status_code
                           if erro_temporario.response is not None
                           else None)
            
            retry = status_code is None or status_code in erros
           
            if not retry or tentativa == tentativas:
                
                logger.error(f"{contexto} | Falha definitiva após "
                             f"{tentativa} tentativas | status={status_code}")
                
                raise RuntimeError(
                    f"Falha após {tentativa} tentativas ao acessar {url}: "
                    f"(status code: {status_code}) {erro_temporario}"
                ) from erro_temporario
            
            espera_atual = espera * (2 ** (tentativa-1))
            
            logger.warning(
                f"{contexto} | Tentativa {tentativa}/{tentativas} "
                f"falhou | status={status_code} | "
                f"aguardando={espera_atual}s"
            )
            
            time.sleep(espera_atual)
             
def salvar_json (pasta, nome_arquivo, dados):
    caminho = DATA/pasta/f'{nome_arquivo}.json'
    
    caminho.parent.mkdir(parents=True, exist_ok=True)
    
    with open(caminho, 'w', encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)
        

def gerar_periodos_ibge(dt_inicio, dt_final):
    
    periodos = []
    dt_atual = dt_inicio
    
    while dt_atual <= dt_final:
        periodos.append(dt_atual.strftime("%Y%m"))
        dt_atual += relativedelta(months=1)
        
    return "|".join(periodos)



