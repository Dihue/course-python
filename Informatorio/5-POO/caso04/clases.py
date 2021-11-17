class Contacto:

	def __init__(self,nombre,telefono,email):
		self.nombre = nombre
		self.telefono = telefono
		self.email = email


	def getNombre(self):
		return self.nombre
	def setNombre(self,nuevoNombre):
		self.nombre = nuevoNombre


	def getTelefono(self):
		return self.telefono
	def setTelefono(self,nuevoTelefono):
		self.telefono = nuevoTelefono


	def getEmail(self):
		return self.email
	def setEmail(self,nuevoEmail):
		self.email = nuevoEmail


	def __str__(self):
		# Funcion para la salida por pantalla de los contactos
		return f"|-> {self.nombre}\t| Tel: {self.telefono}\t| Email: {self.email}"


class Agenda:

	def __init__(self,nombre):
		# Crea una agenda con un nombre y una lista vacia
		self.nombre = nombre
		# Lista de contactos para luego ir agregando
		self.contactos = list()


	# Usado solo para control
	def getNombreAg(self):
		return self.nombre


	def agregar(self,contacto):
		# El contacto lo creo fuera de la clase
		self.contactos.append(contacto)


	def listar(self):
		for c in self.contactos:
			print(c)


	def buscar(self,dato):
		for c in self.contactos:
			if dato == c.getNombre():
				print("\n Contacto/s encontrado/s:\n",c)

			elif dato == str(c.getTelefono()):
				print("\n Contacto/s encontrado/s:\n",c)

			elif dato == c.getEmail():
				print("\n Contacto/s encontrado/s:\n",c)

			else:
				print(" Contacto no encontrado")


	def editar(self,dato,nuevo):
		for c in self.contactos:
			if dato == c.getNombre():
				c.setNombre(nuevo)
				print("\n Contacto editado:\n",c)

			elif dato == str(c.getTelefono()):
				c.setTelefono(nuevo)
				print("\n Contacto editado:\n",c)

			elif dato == c.getEmail():
				c.setEmail(nuevo)
				print("\n Contacto editado:\n",c)


	def salir(self):
		print("\n| --------- HASTA LA PROXIMA --------- |")



'''
Creacion de contacto desde dentro de la clase

def agregarIn(self,nombre,telefono,email):
		c = Contacto(self.nombre,self.telefono,self.email)
		self.contactos.append(c)

No implementado por la escalabilidad del problema(a mi parecer)
'''