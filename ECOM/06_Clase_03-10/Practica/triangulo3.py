class Triangulo:
    EQUILATERO_NOMBRE = "EQUILATERO"
    ISOSCELES_NOMBRE = "ISOSCELES"
    ESCALENO_NOMBRE = "ESCALENO"

    TIPOS = {
        1: EQUILATERO_NOMBRE,
        2: ISOSCELES_NOMBRE,
        3: ESCALENO_NOMBRE
    }
    # Constructor
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    # Métodos
    def tipo_triangulo(self):
        print("Lados:", self.lado1, self.lado2, self.lado3)
        return self.TIPOS[len({self.lado1, self.lado2, self.lado3})]


# Instancias
t1 = Triangulo(2,3,1)
print("Tipo:", t1.tipo_triangulo())

t2 = Triangulo(1,3,1)
print("Tipo:", t2.tipo_triangulo())

t3 = Triangulo(3,3,3)
print("Tipo:", t3.tipo_triangulo())