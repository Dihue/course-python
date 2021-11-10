# Programacion Orienta a Obejtos
# clase
class Persona:

	# Metodo constructor (self: asi mismo)
	def __init__(self, nombre, apellido, edad, dni):
		self.nombre = nombre
		self.apellido = apellido
		self.edad = edad
		self.dni = dni


	# Encapsulamiento
	def getNombre(self):
		# pide el nombre a la persona
		return self.nombre

	def setNombre(self, nuevoNombre):
		# modificar el nombre de la persona
		self.nombre = nuevoNombre

	def getApellido(self):
		return self.apellido

	def setApellido(self, nuevoApellido):
		self.apellido = nuevoApellido

	def __str__(self):
		# Es la forma de mostrarse de un objeto persona (solo por pantalla)
		# Al momento de hacer un print del objeto creado
		return f"Me llamo {self.nombre} {self.apellido} y tengo {self.edad} años"


# Creacion de un objeto persona
p1 = Persona('Dihue','De Cuadra',30,12341234)
p2 = Persona('Damian','Corazza',29,43214321)

#print(type(p1))

print(p1)
print(p2)
print(p1.getNombre())

p2.setApellido('De Cuadra') 
print(p2)


# Otra menera de creacion de objetos
nombre = input("Ingresar nombre: ")
apellido = input("Ingresar apellido: ")
edad = int(input("Ingresar edad: "))
dni = int(input("Ingresar DNI: "))

p3 = Persona(nombre, apellido, edad, dni)

print(p3)

nuevoApellido = input("Apellido real: ")

# Con encapsulamiento
p3.setApellido(nuevoApellido)

print(p3)

# Sin encapsulamiento (no cumple el paradigma)
p1.nombre = 'Dante'

print(p1)