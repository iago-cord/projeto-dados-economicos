import os
import psycopg
from dotenv import load_dotenv
import logging

logger = logging.getLogger(__name__)
load_dotenv()

conn_string = os.getenv('DATABASE_URL')

try:
    with psycopg.connect(conn_string) as conn:
        print("Conexão Estabelecida")
        
        with conn.cursor() as cursor:
            
            cursor.execute("""
                        CREATE TABLE ptax (
                            data TIMESTAMP,
                            cotacao_compra NUMERIC (10,3),
                            cotacao_venda NUMERIC (10,3)
                            );""")
            
            cursor.execute("""
                        CREATE TABLE divida_liquida(
                            data TIMESTAMP,
                            divida_rs NUMERIC (10,2),
                            divida_perc_pib NUMERIC (10,2)
                            );""")
            
            cursor.execute("""
                        CREATE TABLE divida_bruta(
                            data TIMESTAMP,
                            divida_rs NUMERIC (10,2),
                            divida_perc_pib NUMERIC (10,2)
                            );""")
            
            cursor.execute("""
                           CREATE TABLE selic_diaria(
                               data TIMESTAMP,
                               selic_efetiva NUMERIC (10,5),
                               selic_anualizada NUMERIC (10,2),
                               meta_selic NUMERIC (10,2)
                               );""")
            
            cursor.execute("""
                           CREATE TABLE selic_mensal(
                               data TIMESTAMP,
                               selic_acum_anualizada NUMERIC (10,2),
                               selic_acum_mensal NUMERIC (10,2)
                               );""")
            
            cursor.execute("""
                           CREATE TABLE ipca(
                               data TIMESTAMP,
                               var_mensal NUMERIC (10,2),
                               acum_12_meses NUMERIC (10,2)
                               );""")
            
            cursor.execute("""
                           CREATE TABLE atualizacoes(
                               data TIMESTAMP,
                               status VARCHAR(255),
                               qtd_ptax INTEGER,
                               qtd_divida_liquida INTEGER,
                               qtd_divida_bruta INTEGER,
                               qtd_selic_diaria INTEGER,
                               qtd_selic_mensal INTEGER,
                               qtd_ipca INTEGER
                               );""")
            
except Exception as e:
    print('Conexão Falhou')