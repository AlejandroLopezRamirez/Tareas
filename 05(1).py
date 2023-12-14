def convert(data1, data2):
    '''Dadas dos estructuras de datos, data1 y data2,
    devolver data2 convertido al tipo de data1.'''
    clase = type(data1)
    if clase == tuple:
        return tuple(data2)
    if clase == list:
        return list(data2)
    if clase == "class 'set'":
        return set(data2)
    return 'Cagaste amigo'


    #return type(data1)(data2)
