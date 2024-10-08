class Animal:
    # Método abstracto
    def grito(self):
        return NotImplementedError("Método sobreescrito por la herencia")

class Perro(Animal):
    def grito(self):
        return "guau!"

class Gato(Animal):
    def grito(self):
        return "miau!"


perro = Perro()
print(perro.grito())

gato = Gato()
print(gato.grito())