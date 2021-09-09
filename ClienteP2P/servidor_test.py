import socket
import threading
from pickle import dumps, loads
#from multiprocessing import Value
#import time

class HiloServidor(threading.Thread):
    def __init__(self, conexion, direccion):
        threading.Thread.__init__(self)
        self.conexion = conexion
        self.direccion = direccion

    
    def run(self):
        
        print(f"\nNuevo cliente: {self.direccion[0]}")
        
        while True:
            try:
                data = self.conexion.recv(1024)

                decode_data = loads(data)
                print(f"{self.direccion[0]} > {decode_data}")
                self.conexion.sendall(dumps(1))
            except:
                self.conexion.close()
                print('Hilo cerrado')
                break

class ServidorTCP:
    def iniciar():
        hilos =[] #Esta lista contiene todos los hilos creados al conectase varios clientes

        socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        direccion = ('192.168.56.1', 5200)

        socket_server.bind(direccion)
        socket_server.listen(5)
        print(direccion)
        
        print("\nSocket establecido")
        print("\nEsperando...")
        
        while True:
            conexion_socket, direccion = socket_server.accept()
            print(f"Cliente conectado || {direccion}")
            hilo = HiloServidor(conexion_socket, direccion)
            hilo.start()

            print("Hilo para el nuevo cliente almacenado")
            hilos.append(hilo) #Se almacena una 

#ServidorTCP.iniciar()