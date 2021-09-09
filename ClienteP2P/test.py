import socket
servidorDir = ('localhost',8080)
clienteSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clienteSocket.connect(servidorDir)

clienteSocket.sendall(input("Digite algo:").encode())
