'''
Solicite al usuario el ingreso de 3 números, e imprímalos de mayor
a menor.
'''

num1 = int(input("Ingresar primer número: "))
num2 = int(input("Ingresar primer número: "))
num3 = int(input("Ingresar primer número: "))

if (num1 > num2 > num3):
	print(f"De mayor a menor, son: {num1}, {num2}, {num3}")
elif (num3 > num1 > num2):
	print(f"De mayor a menor, son: {num3}, {num1}, {num2}")
elif (num2 > num3 > num1):
	print(f"De mayor a menor, son: {num2}, {num3}, {num1}")
elif (num1 > num3 > num2):
	print(f"De mayor a menor, son: {num1}, {num3}, {num2}")
elif (num3 > num2 > num1):
	print(f"De mayor a menor, son: {num3}, {num2}, {num1}")
elif (num2 > num1 > num3):
	print(f"De mayor a menor, son: {num2}, {num1}, {num3}")