#!/usr/bin/env python3
import sys

def main():
    if len(sys.argv) != 2:
        print("Uso: grava_saudacao.py <nome_arquivo>")
        sys.exit(1)

    nome_arquivo = sys.argv[1]

    # Caminho completo (sem extensão, o Asterisk adiciona .wav)
    caminho = f"/var/lib/asterisk/sounds/saudacao/{nome_arquivo}"

    # RECORD FILE <nome> <formato> <escape_digits> <timeout> [offset samples] [silence] [maxsilence]
    # - formato: WAV  -> 8Khz, mono, 16bits
    # - escape_digits: #  -> usuário pode parar a gravação apertando *
    # - timeout: 30000 ms (30 segundos)
    print(f"RECORD FILE {caminho} wav * 30000")

if __name__ == "__main__":
    main()
