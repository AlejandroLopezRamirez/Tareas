alumnos = [
    {'nombre': 'Juan', 'media': 7.2}, \
    {'nombre': 'Antonio', 'media': 2.5}, \
    {'nombre': 'María', 'media': 8.5} \
]

def aprobados_si_o_no(lista):
    '''
    Recibe una lista de diccionarios con la forma:
    {'nombre': Juan, 'media': 7.2}
    y que devuelva tuplas con True si la media es mayor a 4.5:
    (Juan, True)
    '''
    def auxiliar(dics):
        if len(dics) == 0:
            return
        alum = dics[0]
        res.append((alum['nombre'], alum['media'] >= 4.5))
        auxiliar(dics[1:])
    res = []
    auxiliar(lista)
    return res

def aprobados_lista(lista):
    return[nombre for nombre, aprobado in lista if aprobado]
    