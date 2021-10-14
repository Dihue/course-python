'''
Para el uso de fertilizantes es necesario medir cuánto abarca un
determinado compuesto en el suelo el cual debe existir en una can-
tidad de al menos 10% por hectárea, y no debe existir vegetación
del tipo MATORRAL. Escribir un programa que determine si es facti-
ble la utilización de fertilizantes.
'''

compuesto = int(input("\nPorcentaje del compuesto presente en el suelo: "))
matorral = int(input("\n¿Existencia de matorrales?\n1- SI\n2- NO\n"))

if (compuesto >= 10 and matorral == 2):
	print("Es factible la utilizacion de fertilizantes")
else:
	print("No es factible la utilizacion de fertilizantes")