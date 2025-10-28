#!/usr/bin/env python3
import pymysql
import sys

# Verifica se os dois argumentos foram passados (sala e posição)
if len(sys.argv) != 3:
    print("SET VARIABLE BLOQUEIO 400")  # Código 400 = erro de argumento
    sys.exit(1)

sala = sys.argv[1]
posicao = int(sys.argv[2])  # posição desejada

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
    # Conecta ao banco
    conn = pymysql.connect(**config)
    cursor = conn.cursor()

    # Busca todos os registros da sala
    cursor.execute("SELECT numero, pin FROM sala_geral WHERE num_sala = %s ORDER BY id ASC", (sala,))
    resultados = cursor.fetchall()

    if not resultados:
        print("SET VARIABLE PARTICIPANTE 404")  # Nenhum registro encontrado
        sys.exit(1)

    # Cria os vetores
    numeros = [row['numero'] for row in resultados]
    pins = [row['pin'] for row in resultados]

    # Verifica se a posição é válida
    if posicao < 0 or posicao >= len(numeros):
        print("SET VARIABLE PARTICIPANTE 401")  # Posição inválida
        sys.exit(1)

    # Retorna variáveis para o Asterisk
    print(f"SET VARIABLE PARTICIPANTE 200")
    print(f"SET VARIABLE NUMERO_POSICAO {numeros[posicao]}")
    print(f"SET VARIABLE PIN_POSICAO {pins[posicao]}")

except Exception as e:
    print("SET VARIABLE PARTICIPANTE 500")  # Erro interno
    sys.exit(1)

finally:
    try:
        cursor.close()
        conn.close()
    except:
        pass
