# Primera prueba quitar numeros de una cadena de elementos
# con funciones de orden superior
quita_digito = lambda s:"".join(tuple(filter(lambda x: not x.isdigit() ,s)))

# Lo mismo pero con funcion generadora
quitar_digitos = lambda s:"".join( c for c in s if not s.isdigit())

# Otro que no tenía siendo f una funcion condicional (lambda x > 5) y t una tupla
tomar_mientras = lambda f, t: () if t == () else \
                              () if not f(t[0]) else \
                              (t[0],) + tomar_mientras(f, t[1:])
