# Desarrollar un programa que solicite que te ingresen las ventas
# de 2 dias y que luego se informe por pantalla si se vendio mas
# en el primer dia o en el segundo o si se vendio lo mismo en
# ambos dias.

dia1 = int(input("\nVentas del día 1: "))
dia2 = int(input("\nVentas del día 2: "))

if (dia1 > dia2):
	print("\nSe vendió más el día 1")
elif (dia2 > dia1):
	print("\nSe vendió más el día 2")
elif (dia1 == dia2):
	print("\nSe vendió lo mismo en ambos días")