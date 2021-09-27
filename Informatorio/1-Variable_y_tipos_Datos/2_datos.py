"""
Un DATO es una representacion simbolica (numerica, alfanumerica, etc)
de un atributo o cualidad de una entidad.

Los datos aisladamente pueden no contener informacion pero si los a-
nalizamos en conjunto sirven para realizar calculos o tomar decisiones.

En Python todos los datos son referencias a objetos (no son constantes
ni variables), son como etiquetas para poder identificarlos.

Los objetos en Python pueden ser mutables si pueden modificarse algunas
posiciones del dato o inmutables si no pueden modificarse.

El tipo de un dato esta definido por el conjunto de valores que puede
tomar a lo largo de un programa.

Para ver los tipos de datos, a continuacion usaremos la funcion type()
que nos devuelve el tipo de objeto que enviamos como argumento.
"""

real = 123.23
print(type(real))

complejo = 21.3 + 8j
print(type(complejo))

cadena = "Hola mundo"
print(type(cadena))

booleano = True
print(type(booleano))

conjunto = {'naranja',1,'c', 2.5, True}
print(type(conjunto))

lista = [12.2, 2, "Hola", True]
print(type(lista))

tupla = 12.2, 2, "Hola", True
print(type(tupla))

tupla_anidadda = tupla, 4, False, "Adios"
print(type(tupla_anidadda))

diccionario = {
	1:"Dihue Damian",
	2:"Dizero",
	3:"Didahue"
}
print(type(diccionario))

x = None
print(type(x))