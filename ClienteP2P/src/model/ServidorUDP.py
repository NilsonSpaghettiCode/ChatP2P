from socket import *
import sys
from ..controller.ControladorDirecciones import crear_directorio_usuario
import threading
from pickle import NONE, dumps, loads

class HiloServidorUDP(threading.Thread):
    def __init__(self):
        print("Hilo creado")
    def run(self):
        print("Corriendo hilo")

class ServidorUDP:
    def __init__(self, lista_clientes:list):
        self.direccion = NONE # (ip, puerto)
        self.puerto = 8400
        self.bufsize = 1024
        self.conexion_servidor_udp = True
        self.lista_clientes = lista_clientes
        self.nombre_usuario = 'default'
    
    def getLocal_ip(self):
        return str(gethostbyname(gethostname()))

    def crear_socket_udp(self):
        #Se crea socket de UDP o Datagram
        socket_udp = socket(AF_INET,SOCK_DGRAM)
        self.direccion = self.getLocal_ip()
        #print((self.direccion, self.puerto))
        socket_udp.bind((self.direccion, self.puerto))
        return socket_udp
    # 0    1 
    #(ip,port)
    #         0        1
    #list [('Nombre',(ip, puerto))]
    #                  0    1
    
    def buscar_user(self, direccion:tuple):
        print(self.lista_clientes)
        print("tupla",direccion)
        for cliente in self.lista_clientes:
            print("comparacion",cliente[1][0])
            if cliente[1][0] == direccion[0]:
                nombre_usuario = cliente[0]
                self.nombre_usuario = nombre_usuario
                return True
        else:
            return False
    
    def cerrar_servidor_udp(self):
        
        self.conexion_servidor_udp = False
        print("Intentando cerrar hilo de UDP!")
        exit()
        
                
    
    def iniciar_udp(self):
        while self.conexion_servidor_udp:
            socket_udp = self.crear_socket_udp()
            #print("Esperando audio...")
            data, direccion_cliente = socket_udp.recvfrom(self.bufsize)
            encontrado = self.buscar_user(direccion_cliente)
            #print("Usuario",encontrado)
            if encontrado:
                nombre_archivo = loads(data)
                print ("Archivo recibido:", nombre_archivo)
                
                directorio_de_audio = crear_directorio_usuario(self.nombre_usuario)
                #dirFiles = "./Chat_audio/"+nombre+"/"
                #Direccion del directorio de un audio con el nombre del usuario
                directorio_de_audio = directorio_de_audio+nombre_archivo
                f = open(directorio_de_audio,'wb')
                print("Archivo abierto:"+directorio_de_audio)

                data, direccion_cliente = socket_udp.recvfrom(self.bufsize)
                try:
                    while(data):

                        f.write(data)
                        #print("Recibiendo data...")
                        socket_udp.settimeout(2)
                        #print(len(data))
                        data, direccion_cliente = socket_udp.recvfrom(self.bufsize)

                except timeout:
                    f.close()
                    socket_udp.settimeout(0)
                    socket_udp.close()
                    print ("Archivo descargado...")
            else:
                print('Usuario Denegado')
                socket_udp.close()
        