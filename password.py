claves = []
cont = -1

def credencial(x, y):
    """Devuelve una función que representa una pareja."""
    global cont
    claves.append(y)
    cont=+1
    def get(indice):
        if indice == 0:
            return x
        if indice == 1:
            return cont
    return get

def select(p, i):
    """Devuelve el elemento situado en el índice i de la pareja p."""
    return p(i)

def usuario(credencial):
    """Devuelve el usuario"""
    return select(credencial, 0)

def passwd(credencial):
    """Devuelve la contraseña"""
    return claves[select(credencial, 1)]

usr1=credencial('jaime', 12345)
moduser=usermod()
