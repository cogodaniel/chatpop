#!/usr/bin/env python3
import random

def sortear_sala(inicio=2, fim=5):
    return random.randint(inicio, fim)

if __name__ == "__main__":
    valor = sortear_sala(2, 5)
    print(f"SET VARIABLE SALA_SORTEADA {valor}")
