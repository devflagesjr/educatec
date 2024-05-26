import socket, threading



HOST = '127.0.0.1'
PORT = 15000
CLIENTS = []




def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.bind((HOST, PORT))
        server.listen(1000)
    except:
        print('\nNAO FOI POSSIVEL INICIAR O SERVIDOR...\n')

    while True:
        client, addr = server.accept()
        CLIENTS.append(client)
        thread = threading.Thread(target=trataMensagem, args=[client])
        thread.start()



def trataMensagem(client):
    while True:
        try:
            msg = client.recv(1024)
            broadcast(msg, client)
        except:
            deleteClient(client)
            break




def broadcast(msg, client):
    for clientItem in CLIENTS:
        if clientItem != client:
            try:
                clientItem.send(msg)
            except:
                deleteClient(client)


def deleteClient(client):
    CLIENTS.remove(client)


main()

