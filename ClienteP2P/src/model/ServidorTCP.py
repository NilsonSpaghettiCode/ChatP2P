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

    def getTimeNow(self):
        tiempo_actual = "["+str(datetime.now().strftime("%H:%M:%S"))+"]:"
        return tiempo_actual
        
    def buscar_usuario(self):
        for user in self.lista:
            #print("Comparacion: ",user[1][0])
            #print("Direccion almacenada: ", self.direccion)
            #print(user[0])
            if user[1][0] == self.direccion[0]: #(Nombre, (ip, puerto))
                self.nombre_usuario = user[0]
                return True
                #break
        else:
                return False

    def exterminar_conexion(self):
        try:
            self.conexion.sendall(dumps('1'))    
            print("Confirmacion enviada de sesion")
            self.conexion.close()
        except:
            print("error al enviar")
            self.conexion.close()
            print('Hilo cerrado')
            
    def run(self):
        
        #print(f"\nNuevo cliente: {self.direccion[0]}")
        
        while True:
            try:
                data = loads(self.conexion.recv(1024))
                #print('Nuevo mensaje!')
                if data == '-1':
                    print("Cerrar")
                    self.exterminar_conexion()
                    break
                else:
                    variable = self.buscar_usuario()
                    #print("Usuario: ", variable)
                    #print(self.chats)
                    mensaje = f'{self.nombre_usuario} {self.getTimeNow()} {data}'
                    #print("Mensaje a almacenar:", mensaje.strip())
                    #print("Nombre User:",self.nombre_usuario)
                    self.añadir_mensaje(self.nombre_usuario, mensaje)
                    #print(self.chats[self.nombre_usuario])
                    #print("Responder normal")
                    
                    try:
                        self.conexion.sendall(dumps(data))
                        #print("Confirmacion enviada")
                         
                    except:
                        print("Error al enviar")
                        self.conexion.close()
                        print('Hilo cerrado')
                        break
                    
            except:
                #print(f"{self.direccion[0]} > {decode_data}")
                print("Error al recibir")
                self.conexion.close()
                print('Hilo cerrado')
                break
class ServidorTCP:

    def __init__(self, chats, lista, esta_activo):
        self.chats = chats
        self.lista = lista
        self.esta_activo = esta_activo
    
    @staticmethod
    def getLocal_ip():
        return str(socket.gethostbyname(socket.gethostname()))
        
    def iniciar(self):
        hilos =[] #Esta lista contiene todos los hilos creados al conectase varios clientes

        socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        direccion = (ServidorTCP.getLocal_ip(), 5200)

        socket_server.bind(direccion)
        socket_server.listen(5)
        #print(direccion)
        
        print("\nSocket de escucha establecido")
        #print("\nEsperando...")
        
        while self.esta_activo:
            #print("Activo #1")
            conexion_socket, direccion = socket_server.accept()
            #print("Activo #2")
            #Llamar funcion de hilos que compruebe si esta, si sí, lo deja pasar al usuario por IP, sino, lo agrega como ANONIMO
            #print(f"Cliente conectado || {direccion}")
            hilo = HiloServidor(conexion_socket, direccion, self.chats, self.lista)
            hilo.start()
            
            #print("Hilo para el nuevo cliente almacenado")
            hilos.append(hilo) #Se almacena una 
            hilo.join()
            
    