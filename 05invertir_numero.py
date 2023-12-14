# | Pre:    n >= 0
# {         invertir(n: int) -> int
# | Post:   invertir(n) = el número al revés

#               | n si n < 10
# invertir (n)  {
#               | (n//10) * 10 + (n%10)

digito = lambda n: 1 if n < 10 else 1 + digito(n//10)

invertir = lambda n: n if n < 10 else invertir(n//10) + (n%10) * (10 ** digito(n - 1))
