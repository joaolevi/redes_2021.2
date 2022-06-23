from json import dumps
import socket

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

def Main():
    host = '127.0.0.1'
    port = 8080
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    s.connect((host,port))
    while True:
        print('1. Soma\n2. Subtracao\n3. Multiplicacao\n4. Divisao\n5. Mod\n6. Exponencial\n7. Verificar se eh par\n8. Verificar se eh impar\n9. Logaritmo\n10. Raiz quadrada')
        operacao_id = int(input('Escolha uma operação:'))

        strJson = {}
        if operacao_id in [SOMA_REQUEST_ID, SUBTRACAO_REQUEST_ID, MULTIPLICACAO_REQUEST_ID, DIVISAO_REQUEST_ID,
                        MOD_REQUEST_ID, EXPONENCIAL_REQUEST_ID]:
            num1 = int(input('Primeiro numero: '))
            num2 = int(input('Segundo numero: '))
            strJson = {"e":operacao_id,"num1":num1,"num2":num2}
        elif operacao_id in [EH_PAR_REQUEST_ID, EH_IMPAR_REQUEST_ID, LOGARITMO_REQUEST_ID, RAIZ_QUADRADA_REQUEST_ID]:
            num = int(input('Digite o numero: '))
            strJson = {"e":operacao_id,"num1":num}
        elif operacao_id == EXIT_ID:
            strJson = {"e":operacao_id}
            break
        else:
            print('Nenhuma operacao foi escolhida. Por favor, escolha uma operacao.')
        if strJson != {}:
            message = str(dumps(strJson))
            s.send(message.encode('ascii'))
            data = s.recv(1024)
            print('A resposta dessa operacao é: :', data.decode('UTF-8'))
            ans = input('\nDeseja fazer outra operacao? (s/n) :')
            if ans == 's':
                continue
            else:
                break
    s.close()
 
if __name__ == '__main__':
    Main()