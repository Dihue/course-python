'''
Realiza una función llamada relacion(a, b) que a partir de toneladas recicladas de
dos ciudades se cumpla lo siguiente:

Si el primer número es mayor que el segundo, debe devolver el nombre de la ciudad 1.

Si el primer número es menor que el segundo, debe devolver el nombre de la ciudad 2.

Si ambos números son iguales, debe devolver el nombre de ambas.
'''

def relacion(a,b):
	if a > b:
		print(f"\n{cuidad1} recicló {tonelada1} toneladas")
	elif a < b:
		print(f"\n{cuidad2} recicló {tonelada2} toneladas")
	else:
		print(f"\n{cuidad1} y {cuidad2} reciclaron lo mismo")

cuidad1 = input("\nIngresar el nombre de la cuidad 1: ")
tonelada1 = int(input("\nIngresar cantidad de toneladas recicladas: "))

cuidad2 = input("\nIngresar el nombre de la cuidad 2: ")
tonelada2= int(input("\nIngresar cantidad de toneladas recicladas: "))

relacion(tonelada1,tonelada2)