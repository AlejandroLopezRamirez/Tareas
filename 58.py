def sin_repetidos(lst: list) -> list:
    '''Construye y devuelve una lista
    con los elementos de la original donde se eliminan
    los datos repitidos
    '''
    res = []
    for e in lst:
        if e not in res:
            res.append(e)
    return res
