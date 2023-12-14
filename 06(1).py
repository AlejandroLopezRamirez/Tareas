def add_name(obj, name, value):
    '''Dados tres argumentos (un diccionario obj, una clave
    name y un valor value) devolver un diccionario con
    ese nombre y valor (como pares clave-valor).'''
    res = obj.copy()
    res[name] = value
    return res
