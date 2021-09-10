from pickle import NONE
from src.model.ServidorUDP import ServidorUDP
from src.model.ClienteUDP import ClienteUDP
import sys
from ..view import InterfazChat, InterfazAudio
from ..model.ClienteTCP import ClienteTCP
from .ControladorChat import ControladorChat
from ..model.ServidorTCP import ServidorTCP
import threading
from . import ControladorDirecciones
class ControladorMain:
    #lista = []
    #chats = {}
    #notificacion = False
    #anonimo = False 
    
    def __init__(self,argumentos):
        self.nombre = ""
        self.lista = [] # [('Nombre', (ip, puerto))]
        self.chats = {} # {'Nombre':[]}
        self.contactos = [] # ['Nombre1', 'Nombre2']
        self.servidor_hilos_iniciado = True
        self.servidor_index_conectado = True
        self.estado_servidor_escucha = True
        self.list_obtenida = False
        self.lista_canciones = NONE
        #0 IP index
        #1 Puerto index
        self.argumentos = argumentos
        self.conexionUDP = None
        

    def registar_cliente(self):
        self.nombre = InterfazChat.mostrar_obtener_nombre()
        
    def conectarse_servidor(self):
        conexion_index = ClienteTCP(self.nombre, None,(self.argumentos[1],int(self.argumentos[2])))
        self.servidor_index_conectado = conexion_index.conectarse_server_index()
        self.lista = conexion_index.retornar_lista_usuarios()
        self.list_obtenida = conexion_index.lista_obtenida
            
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
        server = ServidorTCP(self.chats, self.lista, self.estado_servidor_escucha)
        server.iniciar()
        
    def apagar_server_escucha(self):
        self.estado_servidor_escucha = False
        print("Estado cambiado")

    def crear_directorios(self):
        ControladorDirecciones.crear_directorios_audio()
        #ControladorDirecciones.crear_directorio_usuario()
        print("Directorios creados")
        
    def establecer_canciones(self):
        self.lista_canciones = ControladorDirecciones.listar_canciones()
    
    def enviar_texto(self):
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
        
    def enviar_audios(self):
        while True:
            print("")
            self.establecer_canciones()
            InterfazAudio.mostrar_audios(self.lista_canciones)
            #print(self.lista_canciones)
            opcion_audios = InterfazChat.leer_entrada()
            salir = str(len(self.lista_canciones))
            #print("salir",salir)
            #print(opcion_audios)
            if opcion_audios == salir:
                break
            else:
                try:
                    cancion_seleccionada = self.lista_canciones[int(opcion_audios)]
                    while True:
                        contacto_elegido = InterfazChat.entrada_menu_contactos(self.contactos)
                        if contacto_elegido == "Volver" or contacto_elegido == "volver" or contacto_elegido == "VOLVER":
                            break
                        else:
                            for contacto in self.contactos:
                                if contacto == contacto_elegido:
                                    clienteUDP = ClienteUDP(contacto_elegido, self.lista, self.chats, cancion_seleccionada)
                                    clienteUDP.iniciar_envio()
                                    break
                            else:
                                InterfazChat.usuario_incorrecto()
                except:
                    print('La opción digitada es erronea...')
                

    
    def menu_cliente(self):

        while self.servidor_index_conectado:
                    opcion = InterfazChat.entrada_menu_consola(self.nombre)
                    print(opcion)
                    if opcion == "1":
                        while True:
                            #print("Chateando")
                            opcion_chat = InterfazChat.entrada_opcion_de_chat()
                            if opcion_chat == "1": #chat
                               self.enviar_texto()
                            elif opcion_chat == "2": #Audios
                                print("Mandando Audio")
                                self.enviar_audios()
                            elif opcion_chat == "3": #Salir
                                break
                            else:
                                InterfazChat.entrada_incorrecta()
                    elif opcion == "2":
                        print("Saliendo de la aplicacion")
                        self.conexionUDP.cerrar_servidor_udp()
                        
                        sys.exit()         
                    else:
                        InterfazChat.entrada_incorrecta()
                        
    def abrir_conexionUDP(self):
        self.conexionUDP = ServidorUDP(self.lista)
        self.conexionUDP.iniciar_udp()

    def run(self):

        self.registro_conexion()
        if self.list_obtenida:

            self.generar_cc()
            self.crear_directorios()
            
            print("Abrir conexion P2P")
            #self.abrir_conexion_hilos()
            hilo_principal = threading.Thread(target=self.menu_cliente, args=())
            hilo_de_escucha = threading.Thread(target=self.abrir_conexion_hilos,args=())
            hilo_de_escucha_UDP =threading.Thread(target=self.abrir_conexionUDP, args=())
            
            print("Hilo principal arriba")
            hilo_principal.start()
            
            print("Hilo servidor UDP de escucha arriba")
            hilo_de_escucha_UDP.start()

            print("Hilo servidor TCP de escucha arriba")
            hilo_de_escucha.start()

            hilo_principal.join()
            print("Hilo principal cerrado")

            hilo_de_escucha_UDP.join()
            print("Hilo tercero cerrado")
            
            hilo_de_escucha.join()
            print("Hilo segundario cerrado")
            #print(self.servidor_index_conectado)
            
        else:
            print("No se pudo obtener la lista de clientes del servidor index!")

        
