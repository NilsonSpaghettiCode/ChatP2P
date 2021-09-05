import socketserver

class ControladorDatosTCP(socketserver.BaseRequestHandler):
    
    def controlador(self):
        print("Controlando la situacion")