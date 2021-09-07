import socket
from src.model.serializador import serializar_objeto, deserializar_objeto

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('172.19.0.3', 8000)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)
nombre_usuario = str(input('Introduce tu nombre de usuario: '))

sock.sendall(serializar_objeto(nombre_usuario))
try:
    inputX = sock.recv(1024)
    data = deserializar_objeto(inputX)
    print(data)
except:
    print('Algo salio mal...')

sock.close()