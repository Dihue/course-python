
class Triangulo:

	def __init__(self, lado1, lado2, lado3):
		self.lado1 = lado1
		self.lado2 = lado2
		self.lado3 = lado3


	def getLado1(self):
		return self.lado1
	def setLado1(self, newLado1):
		self.lado1 = newLado1

	def getLado2(self):
		return self.lado2
	def setLado2(self, newLado2):
		self.lado2 = newLado2

	def getLado3(self):
		return self.lado3
	def setLado3(self, newLado3):
		self.lado3 = newLado3


	def ladoMayor(self):
		lista_lados = [self.lado1, self.lado2, self.lado3]
		lista_lados.sort()
		return lista_lados[2]


	def tipo(self):
		if self.lado1 == self.lado2 and self.lado1 == self.lado3:
			return "Triángulo equilátero"
		elif self.lado1 != self.lado2 and self.lado2 != self.lado3:
			return "Triángulo escaleno"
		else:
			return "Triángulo isósceles"


L1 = float(input("Ingresar valor del lado 1 del triángulo: "))
L2 = float(input("Ingresar valor del lado 2 del triángulo: "))
L3 = float(input("Ingresar valor del lado 3 del triángulo: "))

triangulo = Triangulo(L1,L2,L3)

print(triangulo.ladoMayor())
print(triangulo.tipo())