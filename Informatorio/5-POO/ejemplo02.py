class Galletitas:
	cantidad = 0

	def __init__(self):
		self.decoracion = False
		Galletitas.cantidad += 1
		print("He cocinado una galletita")

	def hornear(self):
		print("Ya estoy horneada")

	def cambiar_sabor(self):
		self.sabor = "chocolate"

	def __str__(self):
		return f"Esta es la galletita número {Galletitas.cantidad}"


print(Galletitas.cantidad)

# instanciado
galletita = Galletitas()
#print(Galletitas.cantidad)

print(galletita)

galletita.cambiar_sabor()


# instanciado
galletita2 = Galletitas()
#print(Galletitas.cantidad)

print(galletita)