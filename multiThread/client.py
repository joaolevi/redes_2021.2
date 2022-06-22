import socket

def Main():
    host = '127.0.0.1'
    port = 8080
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    s.connect((host,port))
 
    # message = '{"e":1,"num1":3,"num2":5}'
    message = 'Hello'
    while True:
        s.send(message.encode('ascii'))
        data = s.recv(1024)
        print('Received from the server :',str(data.decode('ascii')))
        ans = input('\nDo you want to continue(y/n) :')
        if ans == 'y':
            continue
        else:
            break
    s.close()
 
if __name__ == '__main__':
    Main()