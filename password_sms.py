claves = []
cont = -1

def useradd(x, y):
    """Devuelve una función que representa una pareja."""
    global cont
    claves.append(y)
    cont+=1
    def get(indice):
        if indice == 0:
            return x
        if indice == 1:
            return cont
        return get

def usermod():
    '''blablabla'''
    def select(p, i):
        """Devuelve el elemento situado en el índice i de la pareja p."""
        return p(i)

    def usuario(credencial):
        """Devuelve el usuario"""
        return select(credencial, 0)

    def passwd(credencial):
        """Devuelve la contraseña"""
        return claves[select(credencial, 1)]

    def mensajeria(mensaje):
        '''Paso de mensajes'''
        if mensaje == 'select':
            return select
        if mensaje == 'usuario':
            return usuario
        if mensaje == 'passwd':
            return passwd
        raise ValueError('Mensaje incorrecto')

    return mensajeria
