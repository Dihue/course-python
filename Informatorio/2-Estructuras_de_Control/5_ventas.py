'''
Un locar de remeras vende al por mayor y menor.

Si la compra es por una cantidad mayor o igual a 10 remeras,
el precio por unidad es de tan solo el 80%.

Preguntar cuantas unidades de remeras se incluyen en la com-
pra y el precio por unidad.

Devolver el precio total de la compra

'''

remeras = int(input("\nIndique cantidad de remeras: "))
precio = float(input("\nIngresar el precio por unidad: "))

if (remeras >= 10):
	total = remeras * (precio * 0.8)
else:
	total = remeras * precio

print(f"\nEl precio total de la compra es $ {total}")