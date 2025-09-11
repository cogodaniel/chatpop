#!/usr/bin/env python3

import pymysql
import sys

# Verifica se os dois argumentos foram passados
if len(sys.argv) != 3:
    print("SET VARIABLE MUDO_USUARIO 400")  # Código 400 = erro de argumento
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
        # Verifica se já existe
        sql_select = "SELECT 1 FROM mudo_usuario WHERE numero = %s AND pin = %s LIMIT 1"
        cursor.execute(sql_select, (numero, pin))
        resultado = cursor.fetchone()

        if resultado:
            print("SET VARIABLE INSERE_MUDO_USUARIO 200")  # Já está bloqueado
        else:
            # Insere novo bloqueio
            sql_insert = "INSERT INTO mudo_usuario (numero, pin) VALUES (%s, %s)"
            cursor.execute(sql_insert, (numero, pin))
            conn.commit()
            print("SET VARIABLE INSERE_MUDO_USUARIO 100")  # Novo bloqueio adicionado

    conn.close()
except pymysql.MySQLError as e:
    print("SET VARIABLE INSERE_MUDO_USUARIO 500")  # Erro de banco
    sys.exit(1)
