import xml.etree.ElementTree as ET

arbol = ET.parse('club.xml')
raiz = arbol.getroot()

direccion = raiz.find('.//socio[@id = "1" ]/direccion')
direccion.text = 'Calle Ancha, 35'

arbol.write('club.xml', encoding = 'UTF-8', xml_declaration = True)
