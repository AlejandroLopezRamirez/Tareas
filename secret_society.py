def secret_society(lista):
    '''
    A group of friends have decided to start a secret society.
    The name will be the first letter of each of their names,
    sorted in alphabetical order.
    Create a function that takes in a list of names and returns the name of the secret society.
    '''
    lista2 = sorted(lista)
    nombre = ''
    for i in lista2:
        nombre += i[0].upper()
    return nombre
