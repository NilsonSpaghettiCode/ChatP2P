from pickle import dumps, loads
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
            print(entrada)
            if entrada.lower() == '/exit':
                print('Usted ha cerrado la conexión...')
                self.terminar_conexion()
                break
            else:
                if self.enviar_mensaje(entrada):
                    if not self.recibir_ACK():
                        print("El mensaje no se recibio")
                        self.terminar_conexion()
                        break
                else:
                    print("El mensaje no se envio")
                    self.conexion.close()
                    break
    
    def conectarse_cliente(self):
        clienteTCP = ClienteTCP(self.contacto, (self.direccion_ip_cliente, self.puerto_cliente))
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
        
    def recibir_ACK(self):
        try:
            loads(self.conexion.recv(1024))
            return True
        except:
            return False
    
    def terminar_conexion(self):
        #self.conexion.sendall(dumps(-1))
        self.conexion.close()
    
    def iniciar_chat(self):
        self.retornar_direccion_cliente()
        self.conectarse_cliente()
        self.escribir()
