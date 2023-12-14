import xml.etree.ElementTree as ET

arbol = ET.parse('club.xml')
raiz = arbol.getroot()

socio = raiz.find('.//socio[@id = "1"]')
padre = raiz.find('.//socio[@id = "1"]/..')

