
class Persona:
	def __init__(self, nombre):
		self.nombre = nombre

	def getNombre(self):
		return self.nombre

	def setNombre(self, nuevoNombre):
		self.nombre = nuevoNombre

	def saludar(self):
		return f"Saludos, soy {self.nombre}"


class Alumno(Persona):
	def __init__(self,nombre,legajo):
		super().__init__(nombre)
		self.legajo = legajo

	def getLegajo(self):
		return self.legajo

	def setLegajo(self, nuevoLegajo):
		self.legajo = nuevoLegajo

	def saludar(self):
		return super().saludar() + " y soy alumno/a"


class Profesor(Persona):
	def __init__(self,nombre,materia):
		super().__init__(nombre)
		self.materia = materia

	def getMateria(self):
		return self.materia

	def setMateria(self, nuevoMateria):
		self.materia = nuevoMateria

	def saludar(self):
		return super().saludar() + " y soy profesor/a"


a1 = Alumno("Dihue",20280)
p1 = Profesor("Nico","Programación WEB")

print(a1.getNombre())
print(a1.getNombre())

print(a1.saludar())
print(p1.saludar())

class Vehiculo:
    def __init__ (self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    def getColor(self):
        return self.color
    def getRuedas(self):
        return self.ruedas
    def setColor(self, nuevoColor):
        self.color = nuevoColor
    def setRuedas(self, nuevasRuedas):
        self.ruedas = nuevasRuedas
        
    def mostrar(self):
        return f"El auto {self.color}, tiene: {self.ruedas} ruedas."

class Coche(Vehiculo):

    def __init__(self,color,ruedas,velocidad,cilindrada):
        Vehiculo.__init__(self,color,ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    def mostrar(self):
        return f"El auto {self.color}, tiene: {self.ruedas} ruedas, va a {self.velocidad}, y es de {self.cilindrada} Cilindradas."


A1 = Vehiculo("Verde", 4)
print(A1.mostrar())

A2 = Coche("Azul", 4, 150, 500)
print(A2.mostrar())
