import os
directorio_audios_locales= "./local_audio/"
directorio_audios_recibidos = "./chats_audio/"

def crear_directorios_audio():
    os.makedirs(directorio_audios_locales, exist_ok=True)
    os.makedirs(directorio_audios_recibidos, exist_ok=True)

def crear_directorio_usuario(user):
    dir_user = directorio_audios_recibidos+user+"/"
    os.makedirs(dir_user, exist_ok=True)
    return dir_user

def listar_canciones():
    lista_canciones = []
    with os.scandir(directorio_audios_locales) as canciones:
        for cancion in canciones:
            if cancion.is_file:
                lista_canciones.append(cancion.name)
    return lista_canciones

