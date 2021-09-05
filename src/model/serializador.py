from pickle import dumps, loads

def serializar_lista(lista_usuarios):
    '''
    Esta función serializa el objeto y lo retorna
    '''
    lista_serializada = dumps(lista_usuarios)
    return lista_serializada

def deserializar_lista(objeto_serializado):
    '''
    Esta función deserializa el objeto y lo retorna
    '''
    objeto_deserializado = loads(objeto_serializado)
    return objeto_deserializado
