from src.model.servidor import ServidorTCP

if __name__ == "__main__":
    
    lista_usuarios = []

    direccion_servidor = (ServidorTCP.getLocal_ip(), 8000)
    servidor = ServidorTCP(direccion_servidor,lista_usuarios)
    servidor.iniciar_server()
    
    pass


