#!/usr/bin/env python3

import pymysql
import sys
from datetime import datetime

# Configuração do banco
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'ch@tp0p#11',
    'database': 'chatpop',  # ajuste conforme seu banco
    'cursorclass': pymysql.cursors.DictCursor
}

def main():
    if len(sys.argv) != 5:
        print("Uso: insere_banco_sala.py <NUMERO> <PIN> <SALA> <CANAL>")
        sys.exit(1)

    numero = sys.argv[1]
    pin = sys.argv[2]
    sala = sys.argv[3]
    canal = sys.argv[4]

    try:
        conn = pymysql.connect(**DB_CONFIG)
        cursor = conn.cursor()

        # Verifica se já existe o usuário
        cursor.execute("SELECT * FROM sala_geral WHERE numero=%s AND pin=%s", (numero, pin))
        row = cursor.fetchone()

        if sala.upper() == "SAIR":
            if row:
                cursor.execute("DELETE FROM sala_geral WHERE numero=%s AND pin=%s", (numero, pin))
                conn.commit()
                print(f"[INFO] Usuário {numero} removido da sala.")
            else:
                print(f"[INFO] Usuário {numero} não estava em nenhuma sala.")
        
        else:
            if row:
                cursor.execute("""
                    UPDATE sala_geral
                    SET num_sala=%s, data_hora=%s
                    WHERE numero=%s AND pin=%s AND canal=%s
                """, (sala, datetime.now(), numero, pin, canal))
                conn.commit()
                print(f"[INFO] Usuário {numero} atualizado para sala {sala}.")
            else:
                cursor.execute("""
                    INSERT INTO sala_geral (numero, pin, num_sala, canal)
                    VALUES (%s, %s, %s, %s)
                """, (numero, pin, sala, canal))
                conn.commit()
                print(f"[INFO] Usuário {numero} inserido na sala {sala}.")

    except Exception as e:
        print(f"[ERRO] {e}")
        sys.exit(1)
    finally:
        try:
            cursor.close()
            conn.close()
        except:
            pass

if __name__ == "__main__":
    main()


