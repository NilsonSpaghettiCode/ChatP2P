#Imports
import socket
class Servidor_TCP():
    """
    Esta clase permite instanciar y manejar el servidor indexado
    """
    direccion_servidor = None
    lista_usuario = None

    def __init__(self, direccion_servidor, lista_usuario):
        self.direccion_servidor = direccion_servidor
        self.lista_usuario = lista_usuario
    
    def esta_registrado(self, direccion_usuario):
        """
        Esta función verifica en la estructura de datos "", si la direccion ip ya se encuentra
        registrada.
        """
        return False
        
    def registrar_usuario(self, nombre_usuario):
        """
        Esta funcion registra un usuario en la estructura de datos "".
        """
        print(f"Usuario registrado: {nombre_usuario}")

    def iniciar_server(self):
        servidor_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        servidor_tcp.bind(self.direccion_servidor)
        print("Servidor creado en: ",self.direccion_servidor)

        
        servidor_tcp.listen(5)
        print("Esperando usuario.....")

        conexion_usuario, direccion_usuario = servidor_tcp.accept()
        print("Usuario conectado y aceptado en :",direccion_usuario)

        if self.esta_registrado(direccion_usuario):
            print("Retornando lista de usuarios")
        else:
            print("Registrando usuario")
            print("Retornando lista del usuario")
            
        conexion_usuario.close()


if __name__ == '__main__':

    lista_usuarios = []

    direccion_servidor = ('localhost',8000)
    servidor = Servidor_TCP(direccion_servidor,lista_usuarios)
    servidor.iniciar_server()



