'''
A partir del siguiente diagrama de clases, implementá clases
y métodos para los atributos.
'''

class Vehiculo:
	def __init__(self,color,ruedas):
		self.color = color
		self.ruedas = ruedas

	def getColor(self):
		return self.color
	def setColor(self, nuevoColor):
		self.color = nuevoColor

	def getRuedas(self):
		return self.ruedas
	def setRuedas(self,nuavasRuedas):
		self.ruedas = nuavasRuedas

	def mostrar(self):
		return f"\nTiene {self.ruedas} ruedas y es de color {self.color}."


class Coche(Vehiculo):
	def __init__(self,velocidad,cilindrada,color,ruedas):
		super().__init__(color,ruedas)
		self.velocidad = velocidad
		self.cilindrada = cilindrada

	def getVelocidad(self):
		return self.velocidad
	def setVelocidad(self,nuevaVelocidad):
		self.velocidad = nuevaVelocidad

	def getCilindrada(self):
		return self.cilindrada
	def setCilindrada(self,nuevaCilindrada):
		self.cilindrada = nuevaCilindrada

	def mostrar(self):
		return super().mostrar() + (f" Cuenta con {self.cilindrada} cc y alcanza los {self.velocidad} km/h")


# Objetos
coche1 = Coche(120,1600,"azul",4)

print(coche1.mostrar())
print(type(coche1).__name__)