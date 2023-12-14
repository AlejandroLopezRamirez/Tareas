'''
suma_iter = lambda n, acc: acc if n == 0 else \
                           suma_iter(n//10, acc + n % 10)

suma_digitos = lambda n : suma_iter(n,0)

def suma_digitos(n):
    def aux(n):
        if n < 10:
            return n
        return (n % 10) + aux(n // 10)
    return aux(abs(n))'''

def suma_digitos(n):
    def aux(n):
       suma = 0
        while n > 0:
            resto = n % 10
            n //= 10
        return suma
    return aux(abs(n))
