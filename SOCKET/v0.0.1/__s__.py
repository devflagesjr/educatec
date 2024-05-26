## SERVIDOR 
# BIBLIOTECA SOCKET 
import socket


HOST = '127.0.0.1'
PORT = 15000


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(10)
    conn, addr = s.accept()

    with conn:
        print(f"{addr} > ")
        while True:
            ## Mensagem vinda do cliente
            data = conn.recv(1024).decode("utf-8")
            print(data)
            
            if not data:
                break
            
            ##Mensagem enviada para o cliente
            conn.send(bytes("Ok cleinte, recebido a mensagem", "utf-8"))