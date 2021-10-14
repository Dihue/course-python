'''
Hacer un programa que permita determinar todos los divisores
de un número ingresado por el teclado.
'''

numero = int(input("\nIngresar número: "))

div = 1
lista = []

while (numero >= div):

	if (numero % div) == 0:
		lista.append(div)

	div = div + 1

print(f"\nDivisores del número {numero} son {lista}")

print("1",end=" - ")
for i in range(2, (numero//2+1)):
	if (numero % i == 0):
		print(i,end=" - ")

print(numero)