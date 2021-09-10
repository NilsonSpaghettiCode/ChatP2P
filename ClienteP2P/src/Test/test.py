from socket import *
import sys, os
from pickle import dumps, load, loads
#import select

def mkdir(nombre_user):
    dirUser= f'./Chat_audio/{nombre_user}/'
    os.makedirs(dirUser, exist_ok=True)
    
    return dirUser

#Servidor
host="localhost"
port = 9999

conexion_audio = True
#Aqui
while conexion_audio:
    s = socket(AF_INET,SOCK_DGRAM)
    s.bind((host,port))

    addr = (host, port)
    buf = 1024
    print("Esperando audio")
    data, addr = s.recvfrom(buf)
    nombre_archivo = loads(data)

    print ("Received File:", nombre_archivo)
    nombre = "Nilson"
    dirFileRead = mkdir(nombre)
    #dirFiles = "./Chat_audio/"+nombre+"/"
    dirFileRead = dirFileRead+nombre_archivo

    f = open(dirFileRead,'wb')
    print("Archivo abierto:"+dirFileRead)

    data, addr = s.recvfrom(buf)
    try:
        while(data):

            f.write(data)
            print("Recibiendo data")
            s.settimeout(2)
            #print(len(data))
            data, addr = s.recvfrom(buf)
    except timeout:
        f.close()
        s.settimeout(0)
        s.close()
        print ("File Downloaded")




