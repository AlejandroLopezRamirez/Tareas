SEC1 = 'eikmpqrstuv'
SEC2 = 'pviumterkqs'


def codifica(sec1:str, sec2:str, c:str) -> str:
    '''Codifica un carácter a partir de dos secuencias'''
    i = sec1.find(c)
    return c if i == -1 else sec2[i]


entrada = input('Introduce el texto a codificar: ').lower()
salida = ''.join([codifica(SEC1,SEC2, e) for e in entrada])
print('El texto codificado es:', salida)
