#!/usr/bin/env python3

import pymysql
import sys

# Verifica se os dois argumentos foram passados
if len(sys.argv) != 3:
    print("SET VARIABLE BLOQUEIO 400")  # Código 400 = erro de argumento
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
        sql = "SELECT 1 FROM bloqueio WHERE numero = %s AND pin = %s LIMIT 1"
        cursor.execute(sql, (numero, pin))
        resultado = cursor.fetchone()

        if resultado:
            print("SET VARIABLE BLOQUEIO 100")  # Encontrado
	    #set_var("BLOQUEIO",100)
        else:
            print("SET VARIABLE BLOQUEIO 200")  # Não encontrado
            #set_var("BLOQUEIO",200)

    conn.close()
except pymysql.MySQLError as e:
    print("SET VARIABLE BLOQUEIO 500")  # Erro de conexão/execução
    #set_var("BLOQUEIO",500)
    sys.exit(1)
