#  Escribir un programa que muestre una tabla de multiplicar de tamaño n × n
while True:
    try:
        n = int(input('Introduce un número: '))
        i = 1
        while i <= n:
            j = 1
            while j <= n:
                print(i * j, end = ' ')
                j += 1
            print()
            i += 1
        break
    except ValueError:
        print("Debes escribir un número entero.")
