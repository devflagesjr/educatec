import socket, threading



## Função principal
def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect(('127.0.0.1', 15000))
    except:
        return print('\nNao possivel conectar ao servidor...\n')
    username = input('Usuario>')
    print('\nConectado!!!')


    threadingRecebeMensagem = threading.Thread(target=recebeMenssagens, args=[client])
    threadingEnviaMensagem = threading.Thread(target=envaiMenssagens, args=[client, username])
    threadingRecebeMensagem.start()
    threadingEnviaMensagem.start()





def recebeMenssagens(client):
    while True:
        try:
            msg = client.recv(1024).decode('utf-8')
            print(msg+'\n')
        except:
            print('Nao foi possivel conectar ao servido...')
            print('\nPressiona enter para continuar')
            client.close()
            break





def envaiMenssagens(client, username):
    while True:
        try:
            msg = input('\n')
            client.send(f'<{username}> {msg}'.encode('utf-8'))
        except:
            return




main()