from math import sqrt

def diferencia_diagonal(matriz: dict) -> int:
    '''
    Esta función recibe una matriz cuadrada (mismo número de filas que de columnas)
    y devuelve la diferencia (en valor absoluto) de las sumas de sus diagonales
    '''
    n = int(sqrt(len(matriz)))
    suma_principal = 0
    for i in range (n):
        suma_principal += matriz[(i,i)]
    #suna_principal = sum(matriz[(i,i)] for i in range(n))

    suma_secundaria = 0
    for i in range(n):
        for j in range(n):
            if i + j == n-1:
                suma_secundaria += matriz[(i,j)]
    #suma_secundaria = sum(matriz [(i,j)]    for i in range(n)
    #                                        for j in range(n)
    #                                        if i + j == n - 1)

    return abs(suma_principal - suma_secundaria)
