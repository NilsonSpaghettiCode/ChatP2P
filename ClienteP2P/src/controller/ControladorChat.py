from pickle import NONE, dumps, loads
from ..model.ClienteTCP import ClienteTCP
from ..view import InterfazChat

class ControladorChat:
    def __init__(self, lista, contacto, chat):
        self.direccion_ip_cliente = ""
        self.puerto_cliente = 5200
        self.contacto = contacto
        self.lista = lista
        self.chat = chat
        self.conexion = None

    def escribir(self):
        while not self.conexion == None:
            entrada = InterfazChat.leer_entrada()
            #print("> Yo: ", entrada)
            if entrada == "/exit":
                print("Cerrando")
                self.exterminar_conexion()
                break
            else:
                try:
                    self.conexion.sendall(dumps(entrada))
                    #print('Mensaje enviado con exito')
                except:
                    self.conexion.close()
                    print('Error al enviar')
                    break
                #try:
                    #data = loads(self.conexion.recv(1024))
                    #print("> El: ",data)

                #except:
                    #self.conexion.close()
                    #print('Hilo cerrado')
                    #break
 
    def conectarse_cliente(self):
        clienteTCP = ClienteTCP(self.contacto, (self.direccion_ip_cliente, self.puerto_cliente),NONE)
        self.conexion = clienteTCP.conexion_a_cliente()
        
    def retornar_direccion_cliente(self):
        for usuario in self.lista:
            if usuario[0] == self.contacto:
                self.direccion_ip_cliente = usuario[1][0]
                #print(self.direccion_ip_cliente)
    
    def enviar_mensaje(self, mensaje):
        try:
            self.conexion.sendall(dumps(mensaje))
            return True
        except:
            return False
    
    def exterminar_conexion(self):
        try:
            self.conexion.sendall(dumps('-1'))
            print('Mensaje enviado con exito')         
        except:
            self.conexion.close()
            print('Hilo cerrado')
            
        try:
            data = loads(self.conexion.recv(1024))
            if data == '1':
                self.conexion.close()
                print("Conexion cerrada correctament")
        except:
            self.conexion.close()
            print('Hilo cerrado')
            
    def generar_mensajes_de_chat(self):
        mensajes = self.chat[self.contacto]
        return mensajes       
    
    def iniciar_chat(self):
        self.retornar_direccion_cliente()
        self.conectarse_cliente()
        InterfazChat.mostrar_chat_cliente(self.generar_mensajes_de_chat())
        InterfazChat.mostrar_chat_bienvenido(self.contacto)
        self.escribir()
