from functools import reduce

#La misma funcion de sumar los cuadrados de los primos menores de N but con una expresión generadora

divisores = lambda n: reduce(lambda a, e: a + int(n % e == 0), range(1, n + 1), 0)

es_primo =lambda n: divisores(n) == 2

suma_cuad_primos_menor = lambda n: sum(i ** 2 for i in range(1, n) if es_primo(i))


#Una función generadoraque calcule las parejas de que unos dados sumen 7

dados7 = tuple((x,y) for x in range(1, 7) for y in range(1, 7) if x + y == 7)
