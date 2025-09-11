#!/usr/bin/env python3
import sys
import subprocess

def main():
    if len(sys.argv) != 3:
        print("Uso: muta_canal.py <sala> <canal>")
        sys.exit(1)

    sala = sys.argv[1]
    canal = sys.argv[2]

    comando = f"asterisk -rx 'confbridge mute {sala} {canal}'"

    try:
        resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)
        if resultado.returncode == 0:
            print("Comando executado com sucesso!")
            if resultado.stdout:
                print("Saída:", resultado.stdout.strip())
        else:
            print("Erro ao executar comando:")
            print(resultado.stderr.strip())
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()

