'''
Diseñar un programa que permita obtener el producto entre A y B
mediante sumas sucesivas.
'''

A = int(input("\nValor de A = "))
B = int(input("\nValor de B = "))
producto = 0

'''
while B != 0:
	producto = producto + A
	b = b - 1

print("\nResultado del producto: ", producto)
'''

for i in range(B):
	producto = producto + A

print("\nResultado del producto: ", producto)