
#InterfazChat.leer_entrada()

def entrada_audios():
    print("Digite el número de la cancion, o el número para volver")


def mostrar_audios(lista_audios:list):
    entrada_audios()
   #cancion = lista_audios[x] 
    i = 0
    if(len(lista_audios)>0):
        for elemento in lista_audios:
            print(f'{i}. {elemento}')
            i += 1
        print(f"{i}. Volver")
    else:
        print("No se encontraron audios.")
        print(f"{i}. Volver")


#lista = ['aaa','bbbb','cccc']
#mostrar_audios(lista)