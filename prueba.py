from math import gcd

def racional(x, y):
    '''racional'''
    g = gcd(numer(x), denom(x))
    return racional((numer(x)//g),(denom(x)//g))

def numer(x):
    '''numerador'''
    return x[0]

def denom(x):
    '''denominador'''
    return x[1]

def suma(x, y):
    '''suma'''
    nx, dx = numer(x), denom(x)
    ny, dy = numer(y), denom(x)
    return racional (nx * dy + ny * dx, dx* dy)

def mult(x, y):
    '''multiplica'''
    return racional(numer(x) * numer(y), denom(x) * denom(y))

def iguales(x, y):
    return numer(x) * denom(y) == numer(y) * denom(x)

def imprimir(x):
    print(numer(x), '/', denom(x), sep='')
