import os
nombre = 'Nilson'
dirUser= f'./Chat_audio/{nombre}/'
os.makedirs(dirUser, exist_ok=True)
nombre_recibido = "cancion.mp3"
dircancion= dirUser+nombre_recibido

f = open(dircancion,"wb")

f.write()




