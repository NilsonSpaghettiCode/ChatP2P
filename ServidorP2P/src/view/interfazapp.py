from datetime import datetime
import os

def getTimeNow():
    tiempo_actual = "["+str(datetime.now().strftime("%H:%M:%S"))+"]:"
    return tiempo_actual

def log_creacion_servidor(direccion_servidor):
    print(f"{getTimeNow()} Servidor iniciado en  {direccion_servidor[0]} , en el puerto {direccion_servidor[1]} ")
    
def log_esperar_usuario():
    print(f"{getTimeNow()} Esperando usuario.....")

def log_usuario_conectado(direccion_usuario):
    print(f"{getTimeNow()} Usuario conectado y aceptado en : {direccion_usuario}")

def log_retornar_lista_registrado():
    print(f"{getTimeNow()} Retornando lista de usuarios a un usuario registrado")

def log_registrar_usuario():
    print(f"{getTimeNow()} Registrando usuario")

def log_retornar_lista_nuevo():
    print(f"{getTimeNow()} Retornando lista de los usuarios a un usuario nuevo")

def log_usuarios_lista(lista:list):
    print('<---- Usuarios en la lista ---->')
    for user in lista:
        print(user)
    
def log_usuario_registrado(usuario):
    print(f"{getTimeNow()} Usuario registrado: {usuario}")


