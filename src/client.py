import socket

def Main():
    host = '127.0.0.1'
    port = 8080
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    s.connect((host,port))
    msg_from_server = s.recv(1024)
    print('O servidor diz: ', msg_from_server.decode('UTF-8'))
    while True:
        request = input()
        s.send(request.encode('UTF-8'))
        data = s.recv(1024)
        result = data.decode('UTF-8')
        if result == '\n':
            break
        else:
            print(result)
    s.close()
 
if __name__ == '__main__':
    Main()