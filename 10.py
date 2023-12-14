# 10. Escribir un programa que calcule el máximo común divisor de dos números enteros
# introducidos por teclado, usando:

# a) La función math.gcd.

'''
from math import gcd
while True
    try:
        n1 = int(input('Introduce un número: '))
        n2 = int(input('Introduce otro número: '))
        break
    except ValueError:
        print('el dato introducido no es correcto)
print(gcd(n1, n2))
'''
# b) Bucles.

while True:
    try:
        a = int(input('Introduce un número: '))
        b = int(input('Introduce otro número: '))
        if 0 in (a, b):
            print('No puede haber ningún cero.')
        else:
            break
    except ValueError:
        print('El dato introducido no es correcto')

def mcd(a,b):
    resto = a % b
    if resto == 0:
        return b
    return mcd(b, resto)
print(' El máximo común divisor es', mcd(a, b))

def mcd_bucle(a, b):
    while a % b != 0:
        a, b = b, a % b
    return b
