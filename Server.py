import socket
import time

def Main(): 
    host = ""
    port = 2802

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    server_socket.bind((host, port)) 
    server_socket.listen() 
  
    print("Servidor inicializado na porta " + str(port))

    while True:
        s, addr = server_socket.accept()
        print('Cliente Conectado:')
        jogadaCliente = int(s.recv(1024))
        jogadaServidor = int(input("Digite sua jogada: (0) pedra, (1) papel, (2) tesoura!"))
        time.sleep(1)
        print("Pedra...")
        time.sleep(1)
        print("Papel...")
        time.sleep(1)
        print("Tesoura!!!")
        resultado = verificarJogo(jogadaCliente, jogadaServidor)
        print(resultado)
        s.send(resultado.encode())
        print(jogadaCliente)
        print(jogadaServidor)


def verificarJogo(jogadaCliente, jogadaServidor):
    if(jogadaCliente == 0 and jogadaServidor == 0):
        return "Empate"
    elif(jogadaCliente == 0 and jogadaServidor == 1):
        return "O servidor ganhou"
    elif(jogadaCliente == 0 and jogadaServidor == 2):
        return "O cliente ganhou"
    
    if(jogadaCliente == 1 and jogadaServidor == 0):
        return "O cliente ganhou"
    elif(jogadaCliente == 1 and jogadaServidor == 1):
        return "Empate"
    elif(jogadaCliente == 1 and jogadaServidor == 2):
        return "O servidor ganhou"
    
    if(jogadaCliente == 2 and jogadaServidor == 0):
        return "O servidor ganhou"
    elif(jogadaCliente == 2 and jogadaServidor == 1):
        return "O cliente ganhou"
    elif(jogadaCliente == 2 and jogadaServidor == 2):
        return "Empate"

if __name__ == '__main__': 
    Main()
