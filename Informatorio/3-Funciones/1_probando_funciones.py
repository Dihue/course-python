def iva():
	'''funcion basica para el calculo del IVA'''
	iva = 12
	costo = input("¿Cuál es el monto a calcular?\n")
	calculo = costo * iva / 100

	print(f"El cálculo del IVA es: {calculo}")