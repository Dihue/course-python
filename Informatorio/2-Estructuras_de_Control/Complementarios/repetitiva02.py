'''
Desarrollar una solución que calcule la suma de los cuadrados
de los n primeros números naturales: 1 + 22 + 32 +… + n2
'''

n = int(input("\nIngresar valor de n = "))

# contador
cont = 1
# acumulador
total = 0

for x in range(n):
	x = cont ** 2
	print(f"El cuadrado de {cont} es igual a {x}")
	cont += 1
	total += x

print(f"\nLa sumatoria de los cuadrado es igual a {total}")