def leer_entrada():
    mensaje = str(input('>_ '))
    return mensaje

def mostrar_Menu_registro():
    print("Digite su nombre de registro")

def mostrar_obtener_nombre():
    mostrar_Menu_registro()
    return leer_entrada()

def menu_consola(nombre):
    print("-"*30)
    print(f"¡Bienvenido {nombre} al chat P2P!")
    print("Digite el numero de la opcion")
    #if mensaje:
        #print("-"*30)
        #print(*"Tiene un nuevo mensaje")
    print("-"*30)
    print("1. Chatear")
    print("2. Salir")
    print("-"*30)

def entrada_menu_consola(nombre):
    menu_consola(nombre)
    return leer_entrada()

def menu_contactos(contactos):
    print("Digite el nombre del contacto con el que quiere chatear, sino digite la palabra Volver:")
    j= 1
    print("-"*30)
    for contacto in contactos:
        print(f"{j}. {contacto}")
        j += 1
    print(f"{j}. Volver")
    print("-"*30)

def entrada_menu_contactos(contactos):
    menu_contactos(contactos)
    return leer_entrada()

def opcion_de_chat():
    print("-"*30)
    print("Digite el numero de la opcion")
    print("1. Mensaje de texto")
    print("2. Enviar audio")
    print("3. Volver")
    print("-"*30)

def entrada_opcion_de_chat():
    opcion_de_chat()
    return leer_entrada()

def chat(cliente):
    print(f"!Empiece a chatear con {cliente}!")
    print("Nota: si quiere salir del chat digite /exit")

def entrada_incorrecta():
    print('La opción digitada es incorrecta, intente otra vez...')

def usuario_incorrecto():
    print("-"*30)
    print("El usuario que ingreso no esta registrado")
    print("-"*30)