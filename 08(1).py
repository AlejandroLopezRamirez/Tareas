def integer_boolean(n):
    '''Crear una función que devuelva una lista de valores
    booleanos, a partir de un número dado.
    Repitiendo el dígito del número uno a la vez,
    agregar True si el dígito es 1 y False si es 0.'''
    return [ e == '1' for e in n]
