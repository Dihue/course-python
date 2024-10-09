
# tipo -> equilatero, isosceles, escaleno (depende los lados)
# superficie, perimetro (depende de los lados)
class  Triangulo:
    EQUILATERO_NOMBRE = "EQUILATERO"
    ISOSCELES_NOMBRE = "ISOSCELES"
    ESCALENO_NOMBRE = "ESCALENO"
    TIPOS = {
        1: EQUILATERO_NOMBRE,
        2: ISOSCELES_NOMBRE,
        3: ESCALENO_NOMBRE
    }
    # =====================
    # atributos
    # =====================
    # Forma 1: inicializar atributos
    # lado1 = None
    # lado2 = None 
    # lado3 = None

    # =====================
    # metodos
    # =====================
    def __init__(self, lado1, lado2, lado3):
        # print("estoy en el constructor")
        self.lado1 = lado1 
        self.lado2 = lado2
        self.lado3 = lado3
    """
    def tipo(self):
        print(self.lado1, self.lado2, self.lado3)
        lados = {self.lado1, self.lado2, self.lado3}
        
        print("tipo", lados.__class__.__name__) 
        print("lados", lados) 

        if self.lado1 == self.lado2 == self.lado3: 
            return "Equilátero" 
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3: 
            return "Isósceles" 
        
        return "Escaleno"
    """
    """
    def tipo(self):
        print(self.lado1, self.lado2, self.lado3)
        
        lados = {self.lado1, self.lado2, self.lado3}
        print(len(lados))
        if len(lados) == 1: 
            return "Equilátero" 
        elif len(lados) == 2: 
            return "Isósceles" 
        return "Escaleno"
    """
    def tipo(self):
        # print(self.lado1, self.lado2, self.lado3)
        return self.TIPOS[len({self.lado1, self.lado2, self.lado3})]

if __name__ == "__main__":
    # dict | set
    t1 = Triangulo(3, 3, 3)
    print(t1.tipo())
    print("************************")
    t2 = Triangulo(3, 2, 3)
    print(t2.tipo())
    print("************************")
    t3 = Triangulo(1, 2, 3)
    print(t3.tipo())
