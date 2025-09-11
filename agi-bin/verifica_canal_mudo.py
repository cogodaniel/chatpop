#!/usr/bin/env python3
import socket
import sys
import time

if len(sys.argv) != 2:
    print("Uso: muta_canal_verifica.py <canal>")
    sys.exit(1)

canal = sys.argv[1]

# Configurações AMI
AMI_HOST = "127.0.0.1"
AMI_PORT = 5038
AMI_USER = "gerente"
AMI_PASS = "chatpop"

def conecta_ami(retries=3, delay=0.5):
    for attempt in range(retries):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((AMI_HOST, AMI_PORT))
            time.sleep(0.5)
            return s
        except Exception as e:
            if attempt < retries - 1:
                time.sleep(delay)
            else:
                raise e

def login_ami(sock, retries=3, delay=0.5):
    for attempt in range(retries):
        login_action = f"Action: Login\r\nUsername: {AMI_USER}\r\nSecret: {AMI_PASS}\r\nEvents: off\r\n\r\n"
        sock.sendall(login_action.encode())
        response = sock.recv(1024).decode()
        if "Success" in response:
            return True
        else:
            if attempt < retries - 1:
                time.sleep(delay)
            else:
                raise Exception("Falha no login AMI")
    return False

def mute_channel(sock, canal):
    mute_action = f"Action: MuteAudio\r\nChannel: {canal}\r\nDirection: all\r\nState: on\r\n\r\n"
    sock.sendall(mute_action.encode())
    response = sock.recv(1024).decode()
    return response

def verifica_estado(sock, canal):
    cmd_action = f"Action: Command\r\nCommand: core show channel {canal}\r\n\r\n"
    sock.sendall(cmd_action.encode())
    time.sleep(0.3)
    data = sock.recv(4096).decode()
    # procura a seção -- Streams -- e a linha State
    for line in data.splitlines():
        if line.strip().startswith("State:"):
            state = line.split("State:")[1].strip()
            if state in ["inactive", "sendonly", "recvonly"]:
                return "Mudo"
            elif state == "sendrecv":
                return "Não Mudo"
    return "Desconhecido"

def logout_ami(sock):
    sock.sendall(b"Action: Logoff\r\n\r\n")
    sock.close()

try:
    sock = conecta_ami()
    login_ami(sock)
    mute_channel(sock, canal)
    status = verifica_estado(sock, canal)
    print(f"Canal {canal} está: {status}")
    logout_ami(sock)

except Exception as e:
    print(f"Erro: {e}")
    sys.exit(1)
