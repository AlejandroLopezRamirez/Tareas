#Crea una funcion que devuelva una tupla con los nombres de los alumnos aprobados

media_rec = lambda t, acc, cont: acc / cont if t == () else media_rec(t[1:], acc + t[0], cont + 1)

media = lambda t: media_rec(t, 0, 0)

aprobado = lambda t: media(t) >= 0

antonio = ("Antonio Pérez",(1,4,2))
maria = ("María Rodríguez", (8,7,5))
sonia = ("Sonia González", (9,10))

matriculas = (antonio, maria, sonia)

"""
| Pre: Todos los elementos t de m tienen que cumplir que t[1:][0] != ()
{      aprobados(m:tuple[tuple[str,tuple[floats]]]) -> tuple[str]
|
| Post: aprobados(m) = la tupla que contene los nombres de los aprobados
"""



aprobados = lambda m: () if m == () \
                      else ((m[0][0],) if aprobado(m[0][1:][0]) else ()) + aprobados(m[1:])
