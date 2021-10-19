'''
La ciudad esta dividida en 2 secciones de recolección sección A y B de acuerdo al
nombre de la barrio y el tipo del barrio (CÉNTRICO y NO CÉNTRICO).

La sección A esta formada por los barrios céntricos cuyo nombre comienza con una
letra anterior a M y los barrios no céntricos con nombre posterior a la M, y la
sección B el resto.

Debemos hacer un programa que dado el nombre del barrio y la ubicación, nos infor-
me en que sección se encuentra.
'''

barrio = input("\nIngresar nombre del barrio: ")
ubicacion = input("\nSeleccionar ubicacion del barrio:\n1-Céntrico\n2-No céntrico\n")

if barrio.lower() < 'm' and ubicacion == '1':
	print(f"\nEl barrio {barrio} que es céntrico pertenece a la sección A")

elif barrio.lower() >= 'm' and ubicacion == '2':
	print(f"\nEl barrio {barrio} que no es céntrico pertenece a la sección A")

elif barrio.lower() >= 'm' and ubicacion == '1':
	print(f"\nEl barrio {barrio} que es céntrico pertenece a la sección B")

elif barrio.lower() < 'm' and ubicacion == '2':
	print(f"\nEl barrio {barrio} que no es céntrico pertenece a la sección B")
