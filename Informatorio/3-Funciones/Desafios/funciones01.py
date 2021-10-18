'''
150 años es el tiempo que tarda una bolsa de plástico común en
degradarse y una botella de PET puede tardar 1.000 años en desa-
parecer. 

Por otro lado los Envases de tetrabrik pueden tardar hasta 30 a-
ños en degradarse.

Un trozo de chicle tarda 5 años en degradarse. 

Se solicita una función para que dado el ingreso de un elemento,
se solicite tipo: Bolsa de plástico, botella PET, envase tetra-
brik o chicle, e imprima la cantidad de años que tarda en degra-
darse.
'''


def Tiempo_Degradacion(material):
	if material == '1':
		print("\n150 años en degradarse")
	elif material == '2':
		print("\n1000 años en degradarse")
	elif material == '3':
		print("\n30 años en degradarse")
	elif material == '4':
		print("\n5 años en degradarse")

print("Cantidad de años que tarda un elemento en degradarse")
material = input("\nOpciones:\n1-Bolsa de plástico\n2-Botella PET\n3-Envase de tetrabrik\n4-Chicle\n")

Tiempo_Degradacion(material)