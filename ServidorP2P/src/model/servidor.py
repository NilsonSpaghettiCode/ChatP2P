import socket
from pickle import dumps, loads
from ..view import interfazapp

class ServidorTCP():
    """
    Esta clase permite instanciar y manejar el servidor indexado
    """
    #direccion_servidor = None
    #lista_usuario = []

    def __init__(self, direccion_servidor, lista_usuario):
        self.direccion_servidor = direccion_servidor
        self.lista_usuario = lista_usuario
    
    def esta_registrado(self, direccion_usuario):
        """
        Esta función verifica en la estructura de datos "", si la direccion ip ya se encuentra
        registrada.
        """
        if len(self.lista_usuario) != 0: 
            for usuario in self.lista_usuario:
                if (usuario[1][0] == direccion_usuario[0]):
                    return True

        return False
        
    def registrar_usuario(self, nombre_usuario, direccion_usuario):
        """
        Esta funcion registra un usuario en la estructura de datos "".
        """
        nombre_usuario = nombre_usuario.strip()

        if nombre_usuario == "":
            nombre_usuario = "default " + str(len(self.lista_usuario))
        
        self.lista_usuario.append((nombre_usuario, direccion_usuario))

        interfazapp.log_usuario_registrado(nombre_usuario)

    def retornar_lista_usuario(self,lista_usuarios_serializada,conexion_usuario:socket.socket):
        conexion_usuario.sendall(lista_usuarios_serializada)

    @staticmethod
    def getLocal_ip():
        return str(socket.gethostbyname(socket.gethostname()))
    
    def get_lista(self):
        return self.lista_usuario

    def iniciar_server(self):
        servidor_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        servidor_tcp.bind(self.direccion_servidor)
        interfazapp.log_creacion_servidor(self.direccion_servidor)

        servidor_tcp.listen(5)
        
        #
        while True:
            interfazapp.log_esperar_usuario()
            conexion_usuario, direccion_usuario = servidor_tcp.accept()
            
            interfazapp.log_usuario_conectado(direccion_usuario)
            nombre_usuario = loads(conexion_usuario.recv(1024))

            if self.esta_registrado(direccion_usuario):
                interfazapp.log_retornar_lista_registrado()
                #print(self.lista_usuario, conexion_usuario)
                self.retornar_lista_usuario(dumps(self.lista_usuario), conexion_usuario)
            else:
                interfazapp.log_registrar_usuario()
                self.registrar_usuario(nombre_usuario, direccion_usuario)
                interfazapp.log_retornar_lista_nuevo()
                self.retornar_lista_usuario(dumps(self.lista_usuario), conexion_usuario)
            
            conexion_usuario.close()
            interfazapp.log_usuarios_lista(self.lista_usuario)