# 11. Escribir un programa que determine si un número entero introducido por teclado es
# primo o compuesto.

# Indicación: Un número primo es aquel que sólo puede dividirse exactamente por sí
# mismo y por 1.
'''
n = int(input('Introduzca un número: '))
cont = n - 1
while cont > 1:
    if n % cont == 0:
        print(n, 'no es primo')
        break
    cont -= 1
    if cont == 1:
        print(n, 'es primo')
'''

def es_primo(n):
    def divisores(n):
        res = 0
        i = 1
        while i <= n:
            if n % i == 0:
                res += 1
            i += 1
        return res
    return divisores(n) == 2

while True:
    try:
        num = int(input('Introduzca un número entero: '))
        if num < 2 :
            print('El número debe ser mayor o igual a 2')
        break
    except ValueError:
        print('El dato introducido no es correcto')

if es_primo(num):
    print('El número', num, 'es primo')
else:
    print('El número', num, 'NO es primo')
