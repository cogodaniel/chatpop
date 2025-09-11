#!/usr/bin/env python3
import sys

def proxima_sala(valor_atual: int) -> int:
    if valor_atual >= 5:
        return 1
    else:
        return valor_atual + 1

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: proxima_sala.py <VALOR>")
        sys.exit(1)

    try:
        valor = int(sys.argv[1])
    except ValueError:
        print("Erro: o valor precisa ser um número inteiro.")
        sys.exit(1)

    resultado = proxima_sala(valor)
    print(f"SET VARIABLE PROXIMA_SALA {resultado}")
