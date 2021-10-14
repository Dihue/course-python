'''
Determinar el número mayor de 10 números ingresados
'''
contador = 1
lista = []

while (contador <= 10):
	numero = int(input("\nIngrese un número: "))
	lista.append(numero)
	contador += 1

print("\nEl número mayor es el",max(lista))