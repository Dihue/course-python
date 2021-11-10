'''
Crea al menos un objeto de cada subclase y añadelos a una lista llamada
vehiculos.

Realiza una función llamada catalogar() que reciba la lista de vehículos
y los recorra mostrando el nombre de su clase y sus atributos.

Modifica la función catalogar() para que reciba un argumento optativo
ruedas, haciendo que muestre únicamente los que su número de ruedas
concuerde con el valor del argumento. También debe mostrar un mensaje
"Se han encontrado {} vehículos con {} ruedas:" únicamente si se envía
el argumento ruedas. Ponla a prueba con 0, 2 y 4 ruedas como valor.
'''

class Vehiculo:
	def __init__(self,color,ruedas):
		self.color = color
		self.ruedas = ruedas

	def getRuedas(self):
		return self.ruedas
	def setRueda(self,nuevasRuedas):
		self.ruedas = nuevasRuedas

	def mostrar(self):
		return f"Color: {self.color}\nRuedas: {self.ruedas}"


class Coche(Vehiculo):
	def __init__(self,color,ruedas,velocidad,cilindrada):
		super().__init__(color,ruedas)
		self.velocidad = velocidad
		self.cilindrada = cilindrada

	def mostrar(self):
		return super().mostrar() + (f"\nVelocidad: {self.velocidad}\nCilindrada: {self.cilindrada}")


class Camioneta(Coche):
	def __init__(self,color,ruedas,velocidad,cilindrada,carga):
		super().__init__(color,ruedas,velocidad,cilindrada)
		self.carga = carga

	def mostrar(self):
		return super().mostrar() + (f"\nCarga: {self.carga}")


class Bicicleta(Vehiculo):
	def __init__(self,color,ruedas,tipo):
		super().__init__(color,ruedas)
		self.tipo = tipo

	def mostrar(self):
		return super().mostrar() + (f"\nTipo: {self.tipo}")


class Motocicleta(Bicicleta):
	def __init__(self,color,ruedas,tipo,velocidad,cilindrada):
		super().__init__(color,ruedas,tipo)
		self.velocidad = velocidad
		self.cilindrada = cilindrada

	def mostrar(self):
		return super().mostrar() + (f"\nVelocidad: {self.velocidad}\nCilindrada: {self.cilindrada}")


# Objetos:
auto01 = Coche("azul",4,220,1600)
camio01 = Camioneta("roja",4,140,2300,3500)
bici01 = Bicicleta("blanca",2,"deportiva")
moto01 = Motocicleta("negra",2,"urbana",120,150)

# Lista:
vehiculos = [auto01, camio01, bici01, moto01]


# Funcion catalogar original:
def catalogar(lista):
	for i in lista:
		print("--------------------")
		print(type(i).__name__)
		print(i.mostrar())
		print("--------------------")


# Funcion catalogar modificada:
def catalogarX(lista,ruedas=None):
	cont = 0
	if ruedas != None:
		for i in lista:
			if ruedas == i.getRuedas():
				print("--------------------")
				print(type(i).__name__)
				print(i.mostrar())
				print("--------------------")
				cont += 1
		
		print(f"Se han encontrado {cont} vehículos con {ruedas} ruedas\n")
	else:
		catalogar(lista)


# Llamdo de las distintas variantes de ruedas:
catalogarX(vehiculos,2)
#catalogarX(vehiculos,4)
#catalogarX(vehiculos,0)

# Sin argumento ruedas
#catalogarX(vehiculos)
