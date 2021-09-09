import socket
import threading
from pickle import dumps, loads
from datetime import datetime

class HiloServidor(threading.Thread):
    def __init__(self, conexion, direccion, chats, lista):
        threading.Thread.__init__(self)
        self.conexion = conexion
        self.direccion = direccion
        self.chats = chats #{'Nilson':{['msg1','msg2','msg3']}
        self.lista = lista #[('Nilson',('192.168.1.0',5200))]
        self.nombre_usuario = 'default'
    
    def añadir_mensaje(self, usuario, mensaje):
        self.chats[usuario].append(mensaje)

    def getTimeNow():
        tiempo_actual = "["+str(datetime.now().strftime("%H:%M:%S"))+"]:"
        return tiempo_actual
        
    def buscar_usuario(self):
        for user in self.lista:
            if user[0][1] == self.direccion:
                self.nombre_usuario = user[0]
                return True
                #break
        else:
                return False

    def run(self):
        
        print(f"\nNuevo cliente: {self.direccion[0]}")
        
        while True:
            try:
                data = self.conexion.recv(1024)

                decode_data = loads(data)
                print(f"{self.direccion[0]} > {decode_data}")
                self.conexion.sendall(dumps(1))
                
                self.buscar_usuario(mensaje)
                mensaje = f'{self.nombre_usuario} [{self.getTimeNow()}]: {decode_data}'
                self.añadir_mensaje(self.nombre_usuario, mensaje)
                print(self.chats[self.nombre_usuario])
            except:
                self.conexion.close()
                print('Hilo cerrado')
                break

class ServidorTCP:

    @staticmethod
    def getLocal_ip():
        return str(socket.gethostbyname(socket.gethostname()))
        
    def iniciar(chats, lista):
        hilos =[] #Esta lista contiene todos los hilos creados al conectase varios clientes

        socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        direccion = (ServidorTCP.getLocal_ip(), 5200)

        socket_server.bind(direccion)
        socket_server.listen(5)
        print(direccion)
        
        print("\nSocket establecido")
        print("\nEsperando...")
        
        while True:
            conexion_socket, direccion = socket_server.accept()
            
            #Llamar funcion de hilos que compruebe si esta, si sí, lo deja pasar al usuario por IP, sino, lo agrega como ANONIMO
            print(f"Cliente conectado || {direccion}")
            hilo = HiloServidor(conexion_socket, direccion)
            hilo.start()
            
            print("Hilo para el nuevo cliente almacenado")
            hilos.append(hilo) #Se almacena una 
            hilo.join()