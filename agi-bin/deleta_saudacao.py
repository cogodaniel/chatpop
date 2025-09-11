#!/usr/bin/env python3
import sys
import os

# Caminho base onde os arquivos estão
BASE_PATH = "/var/lib/asterisk/sounds/saudacao/"

def main():
    if len(sys.argv) != 2:
        print("Uso: deleta_saudacao.py <nome_arquivo>")
        sys.exit(1)

    nome_arquivo = sys.argv[1]

    # Adiciona extensão .WAV se não estiver presente
    if not nome_arquivo.lower().endswith(".wav"):
        nome_arquivo += ".wav"

    caminho_completo = os.path.join(BASE_PATH, nome_arquivo)

    try:
        if os.path.isfile(caminho_completo):
            os.remove(caminho_completo)
            print(f"SET VARIABLE ARQUIVO_DELETADO {nome_arquivo}")
        else:
            # Arquivo não encontrado
            print("SET VARIABLE ARQUIVO_DELETADO ")
    except Exception as e:
        # Em caso de erro, retorna vazio
        print("SET VARIABLE ARQUIVO_DELETADO ")

if __name__ == "__main__":
    main()

