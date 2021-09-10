import socket
from pickle import loads, dumps

class ClienteTCP:
    """
    Recibe como parametro nombre del usuario
    @param nombre usuario
    @direccion_index tupla con (ip, port) 
    """
    
    def __init__(self, nombre, direccion_cliente:tuple, direccion_index):
        self.nombre = nombre
        self.direccion_cliente = direccion_cliente
        self.direccion_index = direccion_index
        self.lista = []
        self.esta_conectado = False
        self.lista_obtenida = False
    
    def cliente_socket_conexion(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            print("Intentando conectar a: ",self.direccion_index)
            sock.connect(self.direccion_index)
            self.esta_conectado = True
            print("Conectado")
            return sock
        except:
            print('Error al conectarse')
            self.esta_conectado = False
            return False
    
    def conexion_a_cliente(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sock.connect(self.direccion_cliente)
            return sock
        except:
            print('Error al conectarse')
            return None
    
    def conectarse_server_index(self):
        try:
            sock = self.cliente_socket_conexion()
            sock.sendall(dumps(self.nombre))
            data = loads(sock.recv(1024))
            self.lista = data[:]
            self.lista_obtenida = True
            return True
        except:
            print('Error al enviar o recibir mensaje')
            print('Por favor revise la conexión del servidor indexado')
            return False
                 
    def conectarse_cliente(self, message):
        conexion_cliente = self.conexion_socket()
        conexion_cliente.sendall(dumps(message))  

    def retornar_lista_usuarios(self):
        return self.lista

       