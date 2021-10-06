'''
# Mostrar por pantalla nº desde 1 hasta N, siendo N un nº ingresado

N = int(input("Ingresar el número N: "))

# contador iniciado
i = 1

while (i <= N):
	print(i)
	# contador
	i = i + 1

# Un programa que permita saludar a todos los alumnos de la comision

seguir = 'si'

# lower pasa todo a minuscula
# upper pasa todo a mayusculas
while seguir.lower() == 'si':
	nombre = input("\nIngresar nombre del alumno: ")
	print(f"\nHola alumno {nombre}, muchos éxitos")

	seguir = input("\n¿Desea continuar saludando? Si o No\n")
'''
# rango(valor inicial, valor final, incremento)
# rango(10) = (0,1,2,3,4,5,6,7,8,9)

for variable in range(10,1,-1):
	print(variable)