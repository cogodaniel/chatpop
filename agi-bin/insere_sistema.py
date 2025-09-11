#!/usr/bin/env python3
import sys
import pymysql
from pymysql.err import OperationalError

# Configurações do banco
config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'ch@tp0p#11',
    'database': 'chatpop',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor
}

def main():
    if len(sys.argv) != 3:
        print("Uso: insere_sistema.py <NUMERO> <PIN>")
        sys.exit(1)

    numero = sys.argv[1]
    pin = sys.argv[2]

    try:
        conn = pymysql.connect(**config)
        cursor = conn.cursor()
        query = "INSERT INTO chatpop_sistema (numero, pin) VALUES (%s, %s)"
        cursor.execute(query, (numero, pin))
        conn.commit()
        print(f"✅ Número '{numero}' com PIN '{pin}' inserido com sucesso na tabela chatpop_sistema.")
        cursor.close()
        conn.close()

    except OperationalError as err:
        print(f"Erro de conexão com o banco: {err}")
        sys.exit(1)

if __name__ == "__main__":
    main()

