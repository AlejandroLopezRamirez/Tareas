dicciona = {'nombre': 'Juan', 'notas': [7.5, 3.5, 9.0, 8.6]}
def mediana(dic):
    '''
    Recibe un diccionario con al forma {'nombre': 'Juan', 'notas': [7.5, 3.5, 9.0, 8.6]}
    y devuelve un diccionario con al forma:
    {'nombre': 'Juan', 'notas': [7.5, 3.5, 9.0, 8.6], 'mediana': 8.1}
    '''
    dic2 = dic.copy()
    notas = sorted(dic2['notas'])               #ordeno las notas
    longitud = (len(notas))                     #cuantas notas hay
    medio = longitud // 2                       #saber la mitad para hacer la media luego
    if longitud % 2 == 0:                       #numero par o impar de notas
        mediana = (notas[medio] + notas[medio - 1]) / 2     #sacamos la mediana
    else:
        mediana = notas[medio]                  #sacar la mediana
    dic2['mediana'] = round(mediana, 1)            #lo añadimos todo al diccionario
    return dic2
