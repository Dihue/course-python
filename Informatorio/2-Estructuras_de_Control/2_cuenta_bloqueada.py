# Desarrollar un programa que solicite la cantidad de intentos
# fallidos de ingreso de una contraseña.
# Si la cantidad de mayor a 5 veces, debes informar que la
# cuenta fue bloqueada

ingreso = int(input("Ingrese cantidad de intentos:"))

if ingreso >= 5:
	print("Cuenta bloqueada")
else:
	print("Sesión iniciada")