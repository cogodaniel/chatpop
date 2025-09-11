#!/usr/bin/env python3
import pymysql
import sys

# Configuração do banco de dados
DB_CONFIG = {
    "host": "localhost",
    "user": "root",        # ajuste conforme seu ambiente
    "password": "ch@tp0p#11",   # ajuste conforme seu ambiente
    "database": "chatpop" # ajuste para o banco correto
}

def main():
    if len(sys.argv) != 3:
        print("Uso: retorna_saudacao.py <numero> <pin>")
        sys.exit(1)

    numero = sys.argv[1]
    pin = sys.argv[2]

    try:
        conn = pymysql.connect(**DB_CONFIG)
        cursor = conn.cursor()

        sql = """
        SELECT saudacao FROM saudacao
        WHERE numero = %s AND pin = %s
        LIMIT 1
        """
        cursor.execute(sql, (numero, pin))
        result = cursor.fetchone()

        cursor.close()
        conn.close()

        if result and result[0]:
            nome_arquivo = result[0]
            print(f"SET VARIABLE ARQUIVO_SAUDACAO {nome_arquivo}")
        else:
            # Se não encontrou, devolve vazio
            print("SET VARIABLE ARQUIVO_SAUDACAO sem_saudacao")

    except pymysql.MySQLError as err:
        print(f"SET VARIABLE ARQUIVO_SAUDACAO ")
        sys.exit(1)

if __name__ == "__main__":
    main()
