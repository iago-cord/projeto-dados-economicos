import os
import psycopg
from dotenv import load_dotenv
from pathlib import Path
import pandas as pd 
import logging

logger = logging.getLogger(__name__)

ROOT = Path(__file__).resolve().parent.parent
PROCESSED = ROOT/'data'/'PROCESSED'
BCB = PROCESSED/'BCB'
IBGE = PROCESSED/'IBGE'
CAMBIO = BCB/'CAMBIO'
DIVIDA = BCB/'DIVIDA'
SELIC = BCB/'SELIC'
IPCA = IBGE/'IPCA'


def preparar_dados(caminho, nome_arquivo):
    df = pd.read_parquet(caminho/f'{nome_arquivo}.parquet')
    colunas = df.columns.to_list()
    return df[colunas].itertuples(index=False, name = None)

def insert_dados(conn, dados, tabela, colunas):
    col_table = ", ".join(colunas)
    try:
        with conn.cursor() as cursor:
            with cursor.copy(f'COPY {tabela} ({col_table}) FROM STDIN') as copy:
                for linha in dados:
                    copy.write_row(linha)
        
            logger.info(f'Carga da tabela {tabela} realizada com Sucesso')
            
    except Exception as e:
        
        conn.rollback()
        logger.error(f'Erro ao carregar tabela {tabela}: {e}' , exc_info=True)
        
        raise
    


        
    