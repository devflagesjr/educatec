#__server.py
import socket

##

HOST = "127.0.0.1" ## INICIA O SOCKET PARA TODAS AS INTERFACES 
PORT = 10100 ## PORTA QUE NÂO REQUER SUPER USUARIO


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(100)
    conn, addr = s.accept()
    with conn:
        print(f'CONECTADO AO CLIENTE > {addr}')
        while True:
            dados = conn.recv(1024)
            if not dados:
                break
            print(type(dados))