from math import log2, sqrt
import socket, threading
from json import loads

EXIT_ID                     = 0
SOMA_REQUEST_ID             = 1
SUBTRACAO_REQUEST_ID        = 2
MULTIPLICACAO_REQUEST_ID    = 3
DIVISAO_REQUEST_ID          = 4
MOD_REQUEST_ID              = 5
EXPONENCIAL_REQUEST_ID      = 6
EH_PAR_REQUEST_ID           = 7
EH_IMPAR_REQUEST_ID         = 8
LOGARITMO_REQUEST_ID        = 9
RAIZ_QUADRADA_REQUEST_ID    = 10

class ClientThread(threading.Thread):
    def __init__(self, clientAddress, clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        self.cAddr = clientAddress
        print ("New connection added: ", clientAddress)

    def soma(self, num1, num2):
        return (num1+num2)

    def subtracao(self, num1, num2):
        return (num1-num2)

    def multiplicacao(self, num1, num2):
        return(num1*num2)

    def divisao(self, num1, num2):
        try:
            result = num1/num2
            return(result)
        except Exception as e:
            return (str(e))

    def mod(self, num1, num2):
        resto = num1%num2
        return(resto)

    def exponencial(self, base, expoente):
        return(base**expoente)

    def ehPar(self, num):
        if (num/2) == 0:
            return True
        else:
            return False

    def ehImpar(self, num):
        if (num/2) != 0:
            return True
        else:
            return False

    def logaritmo(self, num):
        return(log2(num))

    def raiz_quadrada(self, num):
        return(sqrt(num))

    def run(self):
        print ("Connection from : ", self.cAddr)
        # self.csocket.send(bytes("Hi, This is from Server..",'utf-8'))
        msg = ''
        while True:
            result = ''
            data = self.csocket.recv(2048)
            msg = data.decode()
            print(msg)
            msg_json = loads(msg)
            if msg_json['e']==SOMA_REQUEST_ID:
                result = self.soma(msg_json['num1'], msg_json['num2'])
            elif msg_json['e']==SUBTRACAO_REQUEST_ID:
                result = self.subtracao(msg_json['num1'], msg_json['num2'])
            elif msg_json['e']==MULTIPLICACAO_REQUEST_ID:
                result = self.multiplicacao(msg_json['num1'], msg_json['num2'])
            elif msg_json['e']==DIVISAO_REQUEST_ID:
                result = self.divisao(msg_json['num1'], msg_json['num2'])
            elif msg_json['e']==MOD_REQUEST_ID:
                result = self.mod(msg_json['num1'], msg_json['num2'])
            elif msg_json['e']==EXPONENCIAL_REQUEST_ID:
                result = self.exponencial(msg_json['num1'], msg_json['num2'])
            elif msg_json['e']==EH_PAR_REQUEST_ID:
                result = self.ehPar(msg_json['num1'])
            elif msg_json['e']==EH_IMPAR_REQUEST_ID:
                result = self.ehImpar(msg_json['num1'])
            elif msg_json['e']==LOGARITMO_REQUEST_ID:
                result = self.logaritmo(msg_json['num1'])
            elif msg_json['e']==RAIZ_QUADRADA_REQUEST_ID:
                result = self.raiz_quadrada(msg_json['num1'])
            elif msg_json['e']==EXIT_ID:
              break
            else:
                print('Nenhuma operacao foi escolhida pelo client.')

            if result != '':
                print('Enviando resposta para o client...')
                self.csocket.send(bytes(f'{result}', 'UTF-8'))
        print ("Client em ", self.cAddr , " desconectado...")
        
def start_server():
    LOCALHOST = "127.0.0.1"
    PORT = 8080
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((LOCALHOST, PORT))
    print("Servidor iniciado")
    print("Esperando a requisição do client..")
    while True:
        server.listen(1)
        clientsock, clientAddress = server.accept()
        newthread = ClientThread(clientAddress, clientsock)
        newthread.start()

if __name__ == '__main__':
    start_server()