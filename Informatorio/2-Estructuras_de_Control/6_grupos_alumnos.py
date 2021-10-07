'''
Los alumnos de un curso se han divido en dos grupos A y B de acuerdo
al sexo y el nombre.

El grupo A esta formado por las mujeres con un nombre anterior a la
M y los hombre con un nombre posterior a la N.

El grupo B por el resto de alumnos. Escribir un programa que le pre-
gunte al usuario su nombre y sexo, y muestre por pantalla el grupo
que le corresponde.
'''

nombre = input("\nIngrese nombre: ")
sexo = input("\nIngrese sexo (F o M): ")
'''
if nombre > 'm' and sexo.lower() == 'm' or nombre <= 'm' and sexo.lower() == 'f':
	print("\n-> Usted pertene al Grupo A")
else:
	print("\n-> Usted pertene al Grupo B")

'''

if sexo.lower() == 'f':

	if nombre.lower() < 'm':
		grupo = "A"
	else:
		grupo = "B"

else:
	if nombre.lower() > 'n':
		grupo = "A"
	else:
		grupo = "B"


print(f"\nUsted pertene al grupo {grupo}")