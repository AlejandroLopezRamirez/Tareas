import random
num = int(input('Introduce un número: '))
sol = random.randint(0,99)

while num != sol:
    if num > sol:
        print('Es demasiado grande.')
        num = int(input('Introduce un número: '))
    else:
        print('Es demasiado pequeño.')
        num = int(input('Introduce un número: '))
print('¡Acertaste!')
