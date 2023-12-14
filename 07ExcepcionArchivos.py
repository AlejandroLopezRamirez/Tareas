try:
    with open('entrada.txt', 'r') as f:
        lineas = f.readlines()
    x, y = [int(x.strip()) for x in lineas]
    suma = x + y
    with open('salida.txt', 'w')as f:
        f.write(str(suma) + '\n')
    print('\nLa operación se ha realizado correctamente\n')
except FileNotFoundError:
    print('Archivo no encontrado')
except ValueError:
    print('Las líneas del archivo deben contener un número entero')
Dado un documento XML como el siguiente (no tiene por qué ser exactamente igual), que representa la información sobre la estructura de una base de datos relacional:

<?xml version="1.0" ?>
<basedatos>
    <tabla>
        <nombre>articulos</nombre>
        <columnas>
            <columna pk="true">
                <nombre>id</nombre>
                <tipo>integer</tipo>
            </columna>
            <columna>
                <nombre>denominacion</nombre>
                <tipo>varchar</tipo>
            </columna>
            <columna>
                <nombre>precio</nombre>
                <tipo>numeric(6,2)</tipo>
            </columna>
        </columnas>
    </tabla>
    <tabla>
        <nombre>clientes</nombre>
        <columnas>
            <columna>
                <nombre>nombre</nombre>
                <tipo>varchar</tipo>
            </columna>
            <columna pk="true">
                <nombre>dni</nombre>
                <tipo>bigint</tipo>
            </columna>
        </columnas>
    </tabla>
</basedatos>
Escribir en Python una función create(archivo) que cargue el archivo XML cuyo nombre se pasa como argumento y que devuelva una cadena que contenga las órdenes SQL necesarias para crear la base de datos indicada.

En el caso del ejemplo anterior, la cadena resultante debe ser:

CREATE TABLE articulos (id integer PRIMARY KEY, denominacion varchar, precio numeric(6,2));
CREATE TABLE clientes (nombre varchar, dni bigint PRIMARY KEY);

Por ejemplo:

Prueba	Resultado
print(create('bd1.xml'))
CREATE TABLE articulos (id integer PRIMARY KEY, denominacion varchar, precio numeric(6,2));
CREATE TABLE clientes (nombre varchar, dni bigint PRIMARY KEY);
print(create('bd2.xml'))
CREATE TABLE alumnos (matricula integer PRIMARY KEY, nombre varchar, apellidos varchar, telefono integer);
CREATE TABLE grupos (grupo varchar PRIMARY KEY);
