from src.controller.ControladorMain import ControladorMain
import sys

if __name__ == "__main__":
    print("Crear controlador")
    #print(sys.argv)
    if(len(sys.argv) == 3):
        controlador = ControladorMain(sys.argv)
        controlador.run()
    else:
        print("Error no ha digitado parametros de ip y puerto")
    #print(controlador.lista)
