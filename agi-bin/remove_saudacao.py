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
    if len(sys.argv) != 4:
        print("Uso: remove_saudacao.py <numero> <pin> <nome_arquivo>")
        sys.exit(1)

    numero = sys.argv[1]
    pin = sys.argv[2]
    nome_arquivo = sys.argv[3]

    try:
        conn = pymysql.connect(**DB_CONFIG)
        cursor = conn.cursor()

        sql_delete = """
        DELETE FROM saudacao
        WHERE numero = %s AND pin = %s AND saudacao = %s
        """
        cursor.execute(sql_delete, (numero, pin, nome_arquivo))
        conn.commit()

        if cursor.rowcount > 0:
            print(f"SET VARIABLE REMOVIDO {nome_arquivo}")
        else:
            # Nenhuma linha deletada
            print("SET VARIABLE REMOVIDO ")

        cursor.close()
        conn.close()

    except pymysql.MySQLError as err:
        # Em caso de erro, retorna vazio
        print("SET VARIABLE REMOVIDO ")
        sys.exit(1)

if __name__ == "__main__":
    main()
