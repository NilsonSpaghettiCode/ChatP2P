from pickle import dumps, loads

def serializar_objeto(objeto):
    lista_serializada = dumps(objeto)
    return lista_serializada

def deserializar_objeto(objeto_serializado):
    objeto_deserializado = loads(objeto_serializado)
    return objeto_deserializado
