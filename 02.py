def str2dic(lista):
    '''
    Recibe una lista de cadenas de la forma "X=Y" (sin espacios),
    donde X es un valor hashable y único
    (es decir, que no se repite como ningún otro valor de X en ninguna otra cadena de la lista)
    e Y es una cadena.
    La función debe devolver un diccionario
    donde la clave de cada elemento será la X y
    el valor asociado a dicha clave será la correspondiente Y.

    Por ejemplo:

    str2dict(['perro=guau', 'gato=miau', 'vaca=mu'])
    == {'perro': 'guau', 'gato': 'miau', 'vaca': 'mu'}
    '''
    return dict([x.split('=') for x in lista])
