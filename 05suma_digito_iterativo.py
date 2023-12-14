suma_iter = lambda n, acc: acc if n == 0 else \
                           suma_iter(n//10, acc + n % 10)

suma_digitos = lambda n : suma_iter(n,0)
