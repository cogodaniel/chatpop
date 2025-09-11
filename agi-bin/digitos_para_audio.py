#!/usr/bin/env python3

import sys

def main():
    if len(sys.argv) != 2:
        print("SET VARIABLE DIGITOS ERRO")
        sys.exit(1)

    valor = sys.argv[1]

    # Transforma cada dígito em numX
    resultado = "&".join([f"num{d}" for d in valor if d.isdigit()])

    print(f"SET VARIABLE DIGITOS {resultado}")

if __name__ == "__main__":
    main()
