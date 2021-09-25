# Alineado con parentesis que abre la funcion

foo = long_function_name(var_one, var_two,
						var_three, var_four)

# Mas identacion para distinguirla del resto

def long_function_name(
		var_one, var_two, var_three,
		var_four):
	print(var_one)


my_list = [
	1,2,3,
	4,5,6,
	7,8,9,
	]

result = some_function_that_takes_arguments(
	'a','b','c',
	'd','e','f',
	)

my_list = [
	1,2,3,
	4,5,6,
	7,8,9,
]

result = some_function_that_takes_arguments(
	'a','b','c',
	'd','e','f',
)


# Asegurate de indentar la linea continuada apropiadamente
# El lugar preferido para cortar alrededor de un operardor
# binario es despues del operardo, no antes
class Rectangle(Blog):

	def __init__(self, width, height,
				color='black', emphasis=None, highlight=0):
		if (width == 0 and height == 0, and
			color == 'red', and emphasis == 'strong' or
			highlight > 100):
			raise ValueError("sorry, you lose")
		if width == 0 and height == 0 and (color == 'red' or
											emphasis is
None):
			raise ValueError("I don't think so -- values are %s, %s")

		Blob.__init__(self, width, height,
					color, emphasis, highlight)

# Las importaciones siempre al principio del archivo
# Luego de cualquier comentario o documentacion
# Siempre antes de variables constantes y globales

import os
import sys
from subprocess import Popen, PIPE

# 1º importaciones de las librerias estandar
# 2º importaciones terceras relacionadas
# 3º importaciones locales de la aplicacion / librerias


# Al importar una clase desde un modulo que contiene una clase,
# generalmente esta bien realizar esto:

from myclass import MyClass
from foo.bar.yourclass import YourClass


# Espacios en blanco en Expresiones y Sentencias

spam(ham[1], {eggs: 2})

if x == 4:
	print x, y; x, y = y, x

spam(1)

dict['key'] = list[index]

x = 1
y = 2
long_variable = 3

i = i + 1
submitted += 1
x = x*2 - 1
hypot = x*x + y*y
c = (a+b) * (a-b)

def complex(real, imag=0.0):
	return magic(r=real, i=imag)


# docstring son comentarios que aparecen luego de la liena "def"
# estos describen la funcion definida, lo que realiza

"""
Return a foobang - descripcion de la funcion
"""
