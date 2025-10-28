#!/usr/bin/env python3
import sys
import os
import pymysql
from datetime import datetime

# Configurações do banco de dados
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'ch@tp0p#11',
    'database': 'chatpop',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor
}

def main():
    # Espera receber parâmetros na ordem:
    # numero_origem pin_origem numero_destino pin_destino
    if len(sys.argv) < 5:
        print("SET VARIABLE TORPEDO erro_parametros")
        sys.exit(1)

    numero_origem = sys.argv[1]
    pin_origem = sys.argv[2]
    numero_destino = sys.argv[3]
    pin_destino = sys.argv[4]

    # Cria nome do arquivo
    data_hora = datetime.now().strftime("%Y%m%d_%H%M%S")
    nome_arquivo = f"{numero_destino}_{pin_destino}_{data_hora}"
    caminho_pasta = "torpedo"
    caminho_arquivo = os.path.join(caminho_pasta, nome_arquivo)

    # Garante que a pasta exista
    os.makedirs(caminho_pasta, exist_ok=True)

    # Insere no banco de dados
    try:
        conn = pymysql.connect(**DB_CONFIG)
        with conn.cursor() as cursor:
            sql = """
            INSERT INTO torpedo (numero_origem, pin_origem, numero_destino, pin_destino, caminho_torpedo)
            VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (numero_origem, pin_origem, numero_destino, pin_destino, caminho_arquivo))
            conn.commit()
    except Exception as e:
        print(f"SET VARIABLE TORPEDO erro_db_{str(e)}")
        sys.exit(1)
    finally:
        if 'conn' in locals():
            conn.close()

    # Retorna variável para o Asterisk
    print(f"SET VARIABLE TORPEDO {caminho_arquivo}")

if __name__ == "__main__":
    main()
