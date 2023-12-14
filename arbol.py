import xml.etree.ElementTree as ET

def create(file_name):
    tree = ET.parse(file_name)
    root = tree.getroot()

    sql_commands = []

    for tabla in root.findall('tabla'):
        table_name = tabla.find('nombre').text
        columns = []

        for columna in tabla.find('columnas').findall('columna'):
            column_name = columna.find('nombre').text
            column_type = columna.find('tipo').text
            pk = "PRIMARY KEY" if columna.get('pk') == 'true' else ""
            column_definition = f"{column_name} {column_type} {pk}"
            columns.append(column_definition)

        columns_str = ', '.join(columns)
        sql_command = f"CREATE TABLE {table_name} ({columns_str});"
        sql_commands.append(sql_command)

    return '\n'.join(sql_commands)

# Ejemplos
print(create('bd1.xml'))
print(create('bd2.xml'))