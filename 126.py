import xml.etree.ElementTree as ET

arbol = ET.parse('club.xml')
raiz = arbol.getroot()

socio = raiz.find('.//socio[@id = "1"]')
telefono = ET.SubElement(socio, 'telefono')
telefono.text = '666555444'

arbol.write('club.xml', encoding = 'UTF-8', xml_declaration = True)
