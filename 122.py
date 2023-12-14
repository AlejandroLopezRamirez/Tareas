import xml.etree.ElementTree as ET
def num_socios():
    '''Cuenta cuantos socios tiene el club del documento
    club.xml y o muestra en pantalla'''

    arbol = ET.parse('club.xml')
    raiz = arbol.getroot()
    cuantos = 0
    for socio in raiz.findall('./socios/socio'):
        cuantos =+ 1
    return cuantos
