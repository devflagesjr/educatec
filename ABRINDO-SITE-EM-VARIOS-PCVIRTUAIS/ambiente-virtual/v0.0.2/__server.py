import socket
import threading

##LISTA DE CLIENTES
clients = []



def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.bind(('127.0.0.1', 2024))
        server.listen(500) #QUANTIDADE MAXIMA DE CONEXÕES
    except:
        return print("\nFalha ao iniciar servidor!!!")

    while True:
        client, addr = server.accept()
        clients.append(client)
        print(client.recv(2048).decode)
    



def mensagensTratamento(client):
    while True:
        try:
            msg = client.recv(2048)
        
        except:
            pass

def broadcast(msg, client):
    try:
        for clientItem in clients:
            if clientItem != client:
                try:
                    clientItem.send(msg)
                except:
                    pass

    except:
        pass


main()