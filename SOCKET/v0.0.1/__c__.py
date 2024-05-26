## CLIENTE
# BIBLIOTECA SOCKET 
import socket


HOST = '127.0.0.1'
PORT = 15000


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as c:
    c.connect((HOST,PORT))
    
    ## Menasgem enviada para o servidor
    c.send(bytes("Olá eu sou o cliente", "utf-8"))
    
    ## Mensagem recebida do servidor
    data = c.recv(1024).decode("utf-8")
    print(data)