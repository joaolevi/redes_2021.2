# server.py

import socket

HOST = "localhost" 
PORT = 1234


def square(num):
    return (num*num)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        conn.send(b'Hello, Client. Send a number!')
        while True:
            data = conn.recv(1024)
            num = data.decode("utf-8")
            if not data:
                break
            result = square(int(num))
            msg = f'The square of {num} is {result}'
            conn.sendall(msg.encode())
