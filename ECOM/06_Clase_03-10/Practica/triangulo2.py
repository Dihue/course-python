class Triangulo:
    # Constructor
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    # Métodos
    def tipo_triangulo(self):
        # Conjunto de datos: SET (no datos repetidos)
        lados = {self.lado1, self.lado2, self.lado3}
        # print("Lados", lados.__class__.__name__)
        print("Lados:", self.lado1, self.lado2, self.lado3)
        
        
        if len(lados) == 1:
            return "Equilátero\n"
        elif len(lados) == 2:
            return "Isósceles\n"
        
        return "Escaleno\n"


# Instancias
t1 = Triangulo(2,3,1)
print("Tipo:", t1.tipo_triangulo())

t2 = Triangulo(1,3,1)
print("Tipo:", t2.tipo_triangulo())

t3 = Triangulo(3,3,3)
print("Tipo:", t3.tipo_triangulo())