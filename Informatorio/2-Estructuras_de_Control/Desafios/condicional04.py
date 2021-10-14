'''
Tenemos que decidir entre 2 recetas ecológicas. Los ingredientes
para cada tipo de receta aparecen a continuación.

Ingredientes comunes: Verduras y berenjena.

Ingredientes Receta 1: Lentejas y apio.

Ingredientes Receta 2: Morrón y Cebolla..

Escribir un programa que pregunte al usuario que tipo de receta
desea, y en función de su respuesta le muestre un menú con los
ingredientes disponibles para que elija. Solo se puede eligir 3
ingrediente (entre la receta elegida y los comunes.) y el tipo
de receta. Al final se debe mostrar por pantalla la receta ele-
gida y todos los ingredientes.
'''

receta = input("\nSeleccione la receta que desea:\n 1-Lentejas y apio\n 2-Morrón y cebolla\n-> ")

if receta == '1':
	ingredientes = "lentejas y apio"
	print("\nSeleccione ingrediente extra para su receta")
	comun = input("\n 1-Verduras\n 2-Berenjena\n 3-Nada\n-> ")

	if comun == '1':
		extra = "verduras"
		print(f"\nSeleccón: Receta 1 de {ingredientes} con {extra}")

	elif comun == '2':
		extra = "berenjena"
		print(f"\nSeleccón: Receta 1 de {ingredientes} con {extra}")

	else:
		print(f"\nSeleccón: Receta 1 de {ingredientes}")

elif receta == '2':
	ingredientes = "morrón y cebolla"
	print("\nSeleccione ingrediente extra para su receta")
	comun = input("\n 1-Verduras\n 2-Berenjena\n 3-Nada\n-> ")

	if comun == '1':
		extra = "verduras"
		print(f"\nSeleccón: Receta 2 de {ingredientes} con {extra}")

	elif comun == '2':
		extra = "berenjena"
		print(f"\nSeleccón: Receta 2 de {ingredientes} con {extra}")

	else:
		print(f"\nSeleccón: Receta 2 de {ingredientes}")
