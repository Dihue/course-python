# Variable:
# 	Espacio en la memoria del ordenador donde se almacenara un valor
# 	que podra cambiar durante la ejecucion del programa.

# El tipo de variable lo define el contenido y no el contenedor

# Todo en Python son objetos

# Enteros (int)
numero_1 = 5	# variable declarada
numero_2 = 3

# Decimales (float)
numero_3 = 2.34

# Operadores
print(numero_1 + numero_2)
print(numero_1 - numero_2)
print(numero_1 * numero_2)
print(numero_1 / numero_2)
print(numero_1 // numero_2)
print(numero_1 ** numero_2)

# Funcion type que devuelve el tipo de la variable
print(type(numero_1))
print(type(numero_3))

# Variable del tipo String
mensaje = """Esto es un mensaje
con saltos
de lineas"""
print(mensaje)

if numero_1 > numero_2:
	print("Si es mayor")
else:
	print("No es mayor")