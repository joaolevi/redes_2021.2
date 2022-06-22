import socket, threading
from json import loads

class ClientThread(threading.Thread):
    def __init__(self, clientAddress, clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        self.cAddr = clientAddress
        print ("New connection added: ", clientAddress)

    def soma(self, num1, num2):
        return (num1+num2)

    def subtracao(self, num1, num2):
        pass

    def multiplicacao(self, num1, num2):
        pass

    def divisao(self, num1, num2):
        pass

    def mod(self, num1, num2):
        pass

    def exponencial(self, num1, num2):
        pass

    def ehPar(self, num):
        pass

    def ehImpar(self, num):
        pass

    def logaritmo(self, num):
        pass

    def raiz_quadrada(self, num):
        pass

    def run(self):
        print ("Connection from : ", self.cAddr)
        # self.csocket.send(bytes("Hi, This is from Server..",'utf-8'))
        msg = ''
        while True:
            data = self.csocket.recv(2048)
            msg = data.decode()
            msg_json = loads(msg)
            if msg_json['e']==1:
                result = self.soma(msg_json['num1'], msg_json['num2'])
                self.csocket.send(bytes(f'the sum result is: {result}', 'utf-8'))
            elif msg_json['e']=='y':
              break
            else:
                self.csocket.send(bytes(msg,'UTF-8'))
        print ("Client at ", self.cAddr , " disconnected...")
        
def start_server():
    LOCALHOST = "127.0.0.1"
    PORT = 8080
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((LOCALHOST, PORT))
    print("Server started")
    print("Waiting for client request..")
    while True:
        server.listen(1)
        clientsock, clientAddress = server.accept()
        newthread = ClientThread(clientAddress, clientsock)
        newthread.start()

if __name__ == '__main__':
    start_server()