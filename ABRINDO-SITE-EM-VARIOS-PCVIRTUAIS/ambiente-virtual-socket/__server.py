import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 1234))
s.listen(5)

while True:
    clientSocket, address = s.accept()
    print(address)
    msg = clientSocket.recv(1024).decode("utf-8")
    clientSocket.send(bytes(f"Bem vindo ao servidor! {msg}", "utf-8"))
