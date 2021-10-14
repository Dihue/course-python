'''
Diseñar un programa que permita calcular el total de una compra,
ingresando cantidad y precio de los productos. El programa debe
estar preparado para que el ingreso de los datos se produzca hasta
que el usuario lo desee.
'''

producto = input("\n¿Desea ingresar un producto?\n1-SI\n2-NO\n\nOpción: ")

cantidad = 0
precio = 0
total = 0

while producto == '1':
	precio = float(input("\nPrecio del producto: "))
	cantidad = int(input("Cantidad del producto: "))

	total = total + (precio * cantidad)

	producto = input("\n¿Desea ingresar otro producto?\n1-SI\n2-NO\n\nOpción: ")

print("\nTotal de la compra es $",round(total,2))