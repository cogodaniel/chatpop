#!/usr/bin/env python3

import pymysql
import sys

# Configuração do banco
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'ch@tp0p#11',
    'database': 'chatpop',  # ajuste conforme necessário
    'cursorclass': pymysql.cursors.DictCursor
}

def contar_participantes(sala):
    try:
        conn = pymysql.connect(**DB_CONFIG)
        with conn.cursor() as cursor:
            # ajusta conforme o nome da tabela e coluna
            sql = "SELECT COUNT(*) AS total FROM sala_geral WHERE num_sala = %s"
            cursor.execute(sql, (sala,))
            result = cursor.fetchone()
            return result['total'] if result and result['total'] else 0
    except Exception as e:
        # Em caso de erro, retorna 0
        return 0
    finally:
        try:
            conn.close()
        except:
            pass

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: num_participantes_sala.py <numero da sala>")
        sys.exit(1)

    sala = sys.argv[1]
    total = contar_participantes(sala)
    print(f"SET VARIABLE NUM_PARTICIPANTES {total}")
