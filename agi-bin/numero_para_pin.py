#!/usr/bin/env python3
import sys

# def ler_variaveis_agi():
#     while True:
#         line = sys.stdin.readline().strip()
#         if line == '':
#             break

def main():
    # ler_variaveis_agi()  # <<-- comente isso

    if len(sys.argv) < 2:
        sys.stderr.write("Uso: gerar_pin.py <NUMERO>\n")
        sys.exit(1)

    numero = sys.argv[1]

    if len(numero) < 6:
        sys.stderr.write("Número muito curto para gerar PIN.\n")
        sys.exit(1)

    pin = numero[:2] + numero[-4:]
    print(f'SET VARIABLE PIN {pin}')
    sys.stdout.flush()

if __name__ == '__main__':
    main()

