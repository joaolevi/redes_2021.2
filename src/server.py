from math import log2, sqrt
import socket, threading

EXIT_REQUEST             = 'SAIR'
SOMA_REQUEST             = 'SOMA'
SUBTRACAO_REQUEST        = 'SUB'
MULTIPLICACAO_REQUEST    = 'MULT'
DIVISAO_REQUEST          = 'DIV'
MOD_REQUEST              = 'MOD'
EXPONENCIAL_REQUEST      = 'EXP'
EH_PAR_REQUEST           = 'PAR'
EH_IMPAR_REQUEST         = 'IMP'
LOGARITMO_REQUEST        = 'LOG'
RAIZ_QUADRADA_REQUEST    = 'SQRT'

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
        if (num%2) == 0:
            return True
        else:
            return False

    def ehImpar(self, num):
        if (num%2) != 0:
            return True
        else:
            return False

    def logaritmo(self, num):
        return(log2(num))

    def raiz_quadrada(self, num):
        return(sqrt(num))

    def run(self):
        print ("Connection from : ", self.cAddr)
        self.csocket.send(bytes(f'Hello, client', 'UTF-8'))
        while True:
            result = ''
            data = self.csocket.recv(2048)
            arrRequest = str(data.decode()).split()
            request = arrRequest[0]

            if request==EXIT_REQUEST:
                    self.csocket.send(bytes('\n', 'UTF-8'))
                    break
            try:
                parametro1 = float(arrRequest[1])
                parametro2 = float(arrRequest[2])

                if request==SOMA_REQUEST:
                    result = self.soma(parametro1, parametro2)
                elif request==SUBTRACAO_REQUEST:
                    result = self.subtracao(parametro1, parametro2)
                elif request==MULTIPLICACAO_REQUEST:
                    result = self.multiplicacao(parametro1, parametro2)
                elif request==DIVISAO_REQUEST:
                    result = self.divisao(parametro1, parametro2)
                elif request==MOD_REQUEST:
                    result = self.mod(parametro1, parametro2)
                elif request==EXPONENCIAL_REQUEST:
                    result = self.exponencial(parametro1, parametro2)
                elif request==EH_PAR_REQUEST:
                    result = self.ehPar(parametro1)
                elif request==EH_IMPAR_REQUEST:
                    result = self.ehImpar(parametro1)
                elif request==LOGARITMO_REQUEST:
                    result = self.logaritmo(parametro1)
                elif request==RAIZ_QUADRADA_REQUEST:
                    result = self.raiz_quadrada(parametro1)      
                else:
                    result = 'Requisicao desconhecida'

                print('Enviando resposta para o client...')
                self.csocket.send(bytes(f'{result}', 'UTF-8'))

            except Exception as e:
                print(str(e)+'\nFaltam parametros na requisicao do client')
                self.csocket.send(bytes('Faltam parametros', 'UTF-8'))



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