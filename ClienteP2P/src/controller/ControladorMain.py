from ClienteP2P.servidor_test import ServidorTCP
from ..view import InterfazChat
from ..model.ClienteTCP import ClienteTCP
from .ControladorChat import ControladorChat
from ..model.ServidorTCP import ServidorTCP

class ControladorMain:
    #lista = []
    #chats = {}
    #notificacion = False
    #anonimo = False 
    
    def __init__(self):
        self.nombre = ""
        self.lista = [] # [('Nombre', (ip, puerto))]
        self.chats = {} # {'Nombre':[]}
        self.contactos = [] # ['Nombre1', 'Nombre2']
        self.servidor_hilos_iniciado = True
        self.servidor_index_conectado = True

    def registar_cliente(self):
        self.nombre = InterfazChat.mostrar_obtener_nombre()
        
    def conectarse_servidor(self):
        conexion_index = ClienteTCP(self.nombre, None)
        self.servidor_index_conectado = conexion_index.conectarse_server_index()
        self.lista = conexion_index.retornar_lista_usuarios()
            
    def registro_conexion(self):
        self.registar_cliente()
        self.conectarse_servidor()
    
    def generar_chats(self):
        for user in self.lista:
            self.chats[user[0]] = []
        print("Chats generadaos")

    def generar_contactos(self):
        self.contactos = self.chats.keys()
    
    def generar_cc(self):
        self.generar_chats()
        self.generar_contactos()

    def abrir_menu_principal(self):
        InterfazChat.menu_contactos(self.chats)
    def abrir_conexion_hilos(self):
        server = ServidorTCP()
        server.iniciar(self.chats,self.lista)

    def run(self):
        self.registro_conexion()
        self.generar_cc()
        print("Abrir conexion P2P")

        #print(self.servidor_index_conectado)

        while self.servidor_index_conectado:
            opcion = InterfazChat.entrada_menu_consola(self.nombre)
            print(opcion)
            if opcion == "1":
                while True:
                    #print("Chateando")
                    opcion_chat = InterfazChat.entrada_opcion_de_chat()
                    if opcion_chat == "1":
                        while True:
                            #print("Mandandando mensaje de texto")
                            opcion_contactos = InterfazChat.entrada_menu_contactos(self.contactos)
                            if opcion_contactos == "Volver" or opcion_contactos == "volver" or opcion_contactos == "VOLVER":
                                break
                            else:
                                for contacto in self.contactos:
                                    if contacto == opcion_contactos:
                                        controlar_chat = ControladorChat(self.lista, opcion_contactos, self.chats)
                                        controlar_chat.iniciar_chat()
                                        break
                                else:
                                    InterfazChat.usuario_incorrecto()

                    elif opcion_chat == "2":
                        print("Mandando Audio")
                    elif opcion_chat == "3":
                        break
                    else:
                        InterfazChat.entrada_incorrecta()
            elif opcion == "2":
                print("Saliendo de la aplicacion")
                break              
            else:
                InterfazChat.entrada_incorrecta()


        

        

