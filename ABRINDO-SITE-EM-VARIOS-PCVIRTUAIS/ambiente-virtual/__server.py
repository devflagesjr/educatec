import socket
import threading


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.bind(('0.0.0.0', 443))
        server.listen(500) #QUANTIDADE MAXIMA DE CONEXÕES
    except:
        return print("\nFalha ao iniciar servidor!!!")

main()