def find_highest(lista):
    '''
    Crea una función que busque el mayor número usando recursión
    '''
    def aux(lista, acc):
        if lista[0] == []:
            aux(lista[1:], lista[0] if lista[0] > lista[1:][0] else lista[1:][0])
        return acc
    aux(lista, [])
 #NO VA
