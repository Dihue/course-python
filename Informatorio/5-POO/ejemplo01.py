class Alumno:

	def __init__(self,nombre):
		self.nombre = nombre
		

	def decir_mi_nombre(self):
		print("Mi nombre es " + self.nombre)

#print("Creo objeto")
x = Alumno(nombre="Pedro")

#print("Asigno nombre")
#x.nombre = 'Juan'

#print(x.nombre)

y = Alumno(nombre="Juan")
#y.nombre = 'Pedro'

#print(y.nombre)

#print("Llamada a las funciones")
print(x.decir_mi_nombre())
print(y.decir_mi_nombre())