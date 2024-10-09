'''
class Triangulo:
    # Constructor
    def __init__(self):
        print("Visualización del constructor")
        self.lado1 = None
        self.lado2 = None
        self.lado3 = None


# Instancia de la clase
t = Triangulo()

# Acceso a los atributos públicos
print("Lado 1: ", t.lado1)
print("Lado 2: ", t.lado2)
print("Lado 3: ", t.lado3)
'''

class Triangulo:
    # Constructor
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    # Métodos
    def tipo_triangulo(self):
        if self.lado1 == self.lado2 == self.lado3:
            return "Equilátero"
        elif self.lado1 == self.lado2 or self.lado2 == self.lado3 or self.lado1 == self.lado3:
            return "Isósceles"
        
        return "Escaleno"


# Instancias de la clase
t1 = Triangulo(2,3,1)
print("Tipo:", t1.tipo_triangulo())

t2 = Triangulo(1,3,1)
print("Tipo:", t2.tipo_triangulo())

t3 = Triangulo(3,3,3)
print("Tipo:", t3.tipo_triangulo())