# Suma de los enteros comprendidos entre a y b

# | Pre:    True
# {         suma (a:int, b:int) -> int
# | Post:   suma(a,b) = la suma de los enteros comprendidos entre a y b

suma_rec = lambda a, b: 0 if a > b else a + suma_rec(a + 1, b)

suma_iter = lambda a, b, acc: acc if a > b else suma_iter(a + 1, b, acc + a)

suma = lambda a, b: suma_iter(a, b, 0)
