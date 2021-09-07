#Imports
import socket
from pickle import dumps, loads

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

        print(f"Usuario registrado: {nombre_usuario}")

    def retornar_lista_usuario(self,lista_usuarios_serializada,conexion_usuario:socket.socket):
        conexion_usuario.sendall(lista_usuarios_serializada)

    def iniciar_server(self):
        servidor_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        servidor_tcp.bind(self.direccion_servidor)
        print("Servidor creado en: ", self.direccion_servidor)

        servidor_tcp.listen(5)
        
        #
        while True:
            print("Esperando usuario.....")
            conexion_usuario, direccion_usuario = servidor_tcp.accept()
            
            print("Usuario conectado y aceptado en :",direccion_usuario)
            nombre_usuario = loads(conexion_usuario.recv(1024))

            if self.esta_registrado(direccion_usuario):
                print("Retornando lista de usuarios a un usuario registrado")
                #print(self.lista_usuario, conexion_usuario)
                self.retornar_lista_usuario(dumps(self.lista_usuario), conexion_usuario)
            else:
                self.registrar_usuario(nombre_usuario, direccion_usuario)
                print("Registrando usuario")
                print("Retornando lista de los usuarios a un usuario nuevo")
                self.retornar_lista_usuario(dumps(self.lista_usuario), conexion_usuario)
            
            conexion_usuario.close()
            print('<---- Usuarios en la lista ---->')
            print(self.lista_usuario)
        
            
if __name__ == "__main__":

    lista_usuarios = []

    direccion_servidor = ("172.19.0.3",8000)
    servidor = ServidorTCP(direccion_servidor,lista_usuarios)
    servidor.iniciar_server()



