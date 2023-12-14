def last_ind(sec):
    '''Una función que devuelve el valor del último
    elemento de una lista o cadena y devuelve none
    si está vacía'''
    try:
        return None if len(sec) == 0 else sec[-1]
    except IndexError:
        return None
