from functools import reduce
#Una funcion que te dice cuantos divisores tiene un número

divisores_map = lambda n: sum(map(lambda e:int(n % e == 0), range (1, n + 1)))

divisores_filter = lambda n: len(tuple(filter(lambda e: n % e == 0, range(1, n+ 1))))

divisores_red = lambda n: reduce(lambda a, e: a + int(n % e == 0), range(1, n + 1), 0)

#Una funcion que te dice si un numero es primo

es_primo = lambda n: divisores_map(n) == 2

#Una funcion que sume el cuadrado de los primos menores que n

sum_cuad_prim_menor = lambda n: reduce(lambda e, ini: e + ini , tuple(map(lambda e: e ** 2, tuple( \
                                                                filter(es_primo,range(1, n))))), 0)
