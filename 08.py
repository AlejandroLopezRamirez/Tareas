dias = {
    'L' : 'Lunes', 'M' : 'Martes', 'X' : 'Miércoles', 'J' : 'Jueves',
    'V' : 'Viernes', 'S' : 'Sábado', 'D' : 'Domingo'
    }
meses = [
    'enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio',
    'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']

def escribir_fecha(dia, ndia, mes, ano):
    '''Mambo'''
    return f'{dias[dia]}, {ndia} de {meses[mes - 1]} de 19{ano}'
