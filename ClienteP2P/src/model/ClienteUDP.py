from socket import *
from pickle import dumps, loads
from ..controller.ControladorDirecciones import *

class ClienteUDP:
    def __init__(self, contacto, lista, chats, cancion):
        self.buffsize = 1024
        self.contacto = contacto
        self.lista = lista
        self.chats = chats
        self.nombre_cancion = cancion
        self.puerto = 8400
    
    def socket_udp_cliente(self):
        socket_udp = socket(AF_INET, SOCK_DGRAM)
        return socket_udp
    
    def obtener_direccion_cliente(self):
        for cliente in self.lista:
            if cliente[0] == self.contacto:
                self.direccion_servidor = cliente[1][0]
                break
                
    
    def enviar_archivo(self, nombre_archivo):
        socket_cliente = self.socket_udp_cliente()
        file_name = directorio_audios_locales+nombre_archivo
        socket_cliente.sendto(dumps(nombre_archivo), (self.direccion_servidor, self.puerto))
        
        file = open(file_name, "rb")

        data = file.read(self.buffsize)

        while (data):
            if (socket_cliente.sendto(data, (self.direccion_servidor, self.puerto))):
                #print('Enviado...')
                data = file.read(self.buffsize)
        print(f"Archivo {nombre_archivo} enviado.")
        file.close()
        socket_cliente.close()

    def iniciar_envio(self):
        self.obtener_direccion_cliente()
        self.enviar_archivo(self.nombre_cancion)
        


