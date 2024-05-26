#__client.py
import socket


## IP SERVER CLOUD 191.252.219.58

HOST = "127.0.0.1"
PORT = 10100


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.send(b"1")