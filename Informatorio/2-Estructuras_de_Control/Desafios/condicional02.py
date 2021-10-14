'''
Para seguir colaborando en esta misión de salvar al planeta, necesitamos
que elabores un programa en Python que dado el tamaño de un pez indique
si su organismo está contaminado. Para ello tendremos 4 opciones:

Tamaño Normal: Mensaje "Pez en buenas condiciones"

Tamaño por debajo de lo Normal: Mensaje "Pez con problemas de nutrición"

Tamaño un poco por encima de lo Normal: Mensaje "Pez con síntomas de
organismo contaminado"

Tamaño sobredimensionado: Mensaje "Pez contaminado"
'''

print("\n¿Cuál es el tamaño del pez?\n")
print("1 - Normal\n2 - Debajo de lo normal\n3 - Por encima de lo normal\n4 - Sobredimensionado\n")

opcion = int(input())

if (opcion == 1):
	print("\nPez en buenas condiciones")
elif (opcion == 2):
	print("\nPez con problemas de nutrición")
elif (opcion == 3):
	print("\nPez con síntomas de organismo contaminado")
elif (opcion == 4):
	print("\nPez contaminado")
