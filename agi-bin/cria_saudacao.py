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
    if len(sys.argv) != 3:
        print("Uso: python3 saudacao.py <usuario> <pin>")
        sys.exit(1)

    usuario = sys.argv[1]
    pin = sys.argv[2]

    # Nome do arquivo
    nome_arquivo = f"saudacao_{usuario}_{pin}"

    # Cria o arquivo
    with open(nome_arquivo, "w") as f:
        f.write(f"Sessão de saudação do usuário {usuario} com pin {pin}\n")

    try:
        conn = pymysql.connect(**DB_CONFIG)
        cursor = conn.cursor()

        # Tenta atualizar primeiro
        sql_update = """
        UPDATE saudacao
        SET saudacao = %s
        WHERE numero = %s AND pin = %s
        """
        cursor.execute(sql_update, (nome_arquivo, usuario, pin))
        conn.commit()

        # Se não atualizou (nenhuma linha encontrada), insere
        if cursor.rowcount == 0:
            sql_insert = """
            INSERT INTO saudacao (numero, pin, saudacao)
            VALUES (%s, %s, %s)
            """
            cursor.execute(sql_insert, (usuario, pin, nome_arquivo))
            conn.commit()

        cursor.close()
        conn.close()

    except pymysql.MySQLError as err:
        print(f"Erro no banco de dados: {err}")
        sys.exit(1)

    # Saída final para o Asterisk
    print(f"SET VARIABLE SAUDACAO {nome_arquivo}")

if __name__ == "__main__":
    main()

