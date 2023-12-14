unicos_aux = lambda secuencia, acc, cont: acc if cont == max(secuencia) + 1 else \
                        unicos_aux(secuencia, \
                        acc + [cont] if secuencia.count(cont) == 1 else acc, \
                        cont + 1)
unicos = lambda secuencia: set(unicos_aux(secuencia, [], 0))

'''
Escribir en Python una función recursiva llamada unicos(secuencia)
que reciba una secuencia de números enteros en la que todos aparecen dos o más veces,
excepto dos de ellos que aparecen exactamente una vez. La función deberá devolver un
conjunto de tipo set que contenga sólo esos dos elementos únicos.

Importante:

La función debe ser pura.
La llamada a la función debe provocar la ejecución de una función
recursiva que genere un proceso iterativo.
No se puede usar ningún bucle while, for, definiciones por comprensión ni expresiones generadoras.

Por ejemplo:

unicos([1, 9, 8, 8, 7, 6, 1, 6]) == {7, 9}
'''
