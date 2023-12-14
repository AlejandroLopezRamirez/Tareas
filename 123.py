import xml.etree.ElementTree as ET

arbol = ET.parse('club.xml')
raiz = arbol.getroot()

for socio in raiz.iter('socio'):
    direccion = socio.find('direccion')
    direccion.text = 'Avda. de Huelva, s/n'
arbol.write('club.xml', encoding = 'UTF-8', xml_declaration = True)
