# Conjunto de lineas de codigo agrupadas que funcionan como una unidad
# realizando una tarea en especifico

# Las funciones pueden o no devolver valores

# Las funciones pueden tener parametros/argumentos

# A las funciones tambien se las denomina "metodos" cuando se encuentran
# definidas dentro de una clase

# Declaracion de una funcion
def mensaje():
	print("Estamos aprendiendo Python")

# Llamado de la funcion para darle uso
mensaje()

# Funcion con parametros
def suma(num1, num2):
	print(num1 + num2)

# Llamada con parametros
suma(2,3)

# Funcion con parametros y devolucion de variable
def resta(num1,num2):
	resultado = num1 - num2
	return resultado

print(resta(32,2))

# Python pasa los valores siempre por REFERENCIA