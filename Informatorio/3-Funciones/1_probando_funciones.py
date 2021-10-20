def iva():
	'''funcion basica para el calculo del IVA del 21%'''
	iva = 21
	costo = float(input("¿Cuál es el monto a calcular?\n $ "))
	calculo = costo * iva / 100

	print(f"\nEl cálculo del IVA es: ${round(calculo,2)}")


def suma(numero1,numero2):
	'''funcion la cual suma dos numeros'''
	print(numero1 + numero2)
	print("\n")


def imprime_fibonacci(n):
	'''escribe la funcion de fibonacci'''
	a = 0
	b = 1

	while (b < n):
		print(b, end=" ")
		a = b
		b = a + b


def devuelve_fibonacci(n):
	'''devuelve la sucesion de Fibonacci hasta n'''
	resultado = []
	a = 0
	b = 1

	while (b < n):
		resultado.append(b)
		a = b
		b = a + b

	return resultado


# Uso de las funciones

mensaje = "\nCalcular el IVA de un monto\n"
print(mensaje)

iva()


mensaje1 = "\nSuma de dos números es:"
print(mensaje1)

suma(13,37)


mensaje2 = "Sucesión de Fibonacci"
print(mensaje2)

print("\nLa sucesión de Fibonacci hasta 10 es:", imprime_fibonacci(10))

print(f"\nLa sucesión de Fibonacci hasta 50 es: {devuelve_fibonacci(50)}")