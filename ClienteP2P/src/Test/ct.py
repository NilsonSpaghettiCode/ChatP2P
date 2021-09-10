from socket import *
import sys
from pickle import dumps, loads

#Cliente
s = socket(AF_INET,SOCK_DGRAM)
host = 'localhost'
port = 9999
buf = 1024
addr = (host,port)

name_archivo = "c6.m4a"
file_name = './Local Audios/'+name_archivo

#file_name += str(input('Introduzca el nombre del audio: '))

s.sendto(dumps(name_archivo), addr)

f=open(file_name, "rb")

data = f.read(buf)
while (data):
    if(s.sendto(data,addr)):
        print ("sending ...")
        data = f.read(buf)
s.close()
f.close()