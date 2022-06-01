# echo-client.py

import socket

HOST = "localhost"  # The server's hostname or IP address
PORT = 1234  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    data = s.recv(1024)
    print(data.decode('utf-8'))
    number = input('Number: ')
    s.sendall(number.encode())
    result = s.recv(1024)
print(f"Server response: {result.decode('utf-8')}")