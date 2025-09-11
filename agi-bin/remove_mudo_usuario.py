#!/usr/bin/env python3

import pymysql
import sys

# Verifica se os dois argumentos foram passados
if len(sys.argv) != 3:
    print("SET VARIABLE REMOVE_MUDO 400")  # Código 400 = erro de argumento
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
        # Verifica se o registro existe
        sql_select = "SELECT 1 FROM mudo_usuario WHERE numero = %s AND pin = %s LIMIT 1"
        cursor.execute(sql_select, (numero, pin))
        resultado = cursor.fetchone()

        if resultado:
            # Remove o registro
            sql_delete = "DELETE FROM mudo_usuario WHERE numero = %s AND pin = %s"
            cursor.execute(sql_delete, (numero, pin))
            conn.commit()
            print("SET VARIABLE REMOVE_MUDO 100")  # Registro removido com sucesso
        else:
            print("SET VARIABLE REMOVE_MUDO 200")  # Registro não encontrado

    conn.close()
except pymysql.MySQLError as e:
    print("SET VARIABLE REMOVE_MUDO 500")  # Erro de banco
    sys.exit(1)

