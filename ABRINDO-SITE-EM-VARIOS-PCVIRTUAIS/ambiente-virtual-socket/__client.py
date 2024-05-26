import socket

HOST = "191.252.219.58"
LOCAL = "0.0.0.0"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("191.252.219.58", 1234))

s.send(bytes("1", "utf-8"))

#msg = s.recv(1024)
#decode = msg.decode("utf-8")

#print(decode)