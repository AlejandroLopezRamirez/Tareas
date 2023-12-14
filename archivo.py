import xml.etree.ElementTree as ET

def procesar_xml(archivo_xml):
    # Cargar el archivo XML
    tree = ET.parse(archivo_xml)
    root = tree.getroot()

    # Procesar el archivo XML
    for elemento in root:
        # Realizar las operaciones deseadas con los elementos XML
        print(f"Elemento: {elemento.tag}, Valor: {elemento.text}")

# Ejemplo de uso
procesar_xml("archivo.xml")