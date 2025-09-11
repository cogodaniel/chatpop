#!/usr/bin/env python3

import pymysql
import sys

# Verifica se os dois argumentos foram passados
if len(sys.argv) != 3:
    print("SET VARIABLE CANAL 400")  # Código 400 = erro de argumento
    sys.exit(1)

numero = sys.argv[1]
pin = sys.argv[2]

# Configurações do banco
config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'ch@tp0p#11',
    'database': 'chatpop',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor
}

try:
    conn = pymysql.connect(**config)
    with conn.cursor() as cursor:
        # Busca o canal correspondente
        sql_select = """
            SELECT canal 
            FROM sala_geral 
            WHERE numero = %s AND pin = %s
            ORDER BY data_hora DESC
            LIMIT 1
        """
        cursor.execute(sql_select, (numero, pin))
        resultado = cursor.fetchone()

        if resultado and resultado["canal"]:
            print(f"SET VARIABLE CANAL {resultado['canal']}")
        else:
            print("SET VARIABLE CANAL 200")  # Não encontrado

    conn.close()
except pymysql.MySQLError:
    print("SET VARIABLE CANAL 500")  # Erro no banco
    sys.exit(1)
