import socket 

def Main(): 

    host = '127.0.0.1'
    port = 2802

    while True:

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        dest = (host, port) 
        
        client_socket.connect(dest)

        msg = input("Digite sua jogada: (0) pedra, (1) papel, (2) tesoura!")

        client_socket.send(msg.encode())
        
        try:
            resposta, servidor = client_socket.recvfrom(1024)
            print('Resposta do Servidor: ', resposta.decode())
        except: 
            print('Ocorreu um erro...')
            client_socket.close()#Fecha a conexão com o servidor
    
    

if __name__ == '__main__': 
	Main()