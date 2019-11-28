import socket
import time

HOST = '172.20.128.201'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = input()
            var = bytes(data, "utf-8")
            if not data:
                break
            conn.sendall(var)