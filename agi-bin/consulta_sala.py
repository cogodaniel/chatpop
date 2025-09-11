#!/usr/bin/env python3

import pymysql
import sys

# Configuração do banco
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'ch@tp0p#11',
    'database': 'chatpop',  # ajuste conforme seu banco
    'cursorclass': pymysql.cursors.DictCursor
}

def main():
    if len(sys.argv) != 3:
        print("SET VARIABLE SALA_ATUAL NAO_ENCONTRADO")
        sys.exit(1)

    numero = sys.argv[1]
    pin = sys.argv[2]

    try:
        conn = pymysql.connect(**DB_CONFIG)
        cursor = conn.cursor()

        cursor.execute("SELECT num_sala FROM sala_geral WHERE numero=%s AND pin=%s", (numero, pin))
        row = cursor.fetchone()

        if row:
            print(f"SET VARIABLE SALA_ATUAL {row['num_sala']}")
        else:
            print("SET VARIABLE SALA_ATUAL NAO_ENCONTRADO")

    except Exception as e:
        print(f"SET VARIABLE SALA_ATUAL ERRO")
        sys.exit(1)
    finally:
        try:
            cursor.close()
            conn.close()
        except:
            pass

if __name__ == "__main__":
    main()
