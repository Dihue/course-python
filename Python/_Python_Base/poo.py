class Punto:
    def __init__(self, x, y):
        # Atributos "privados" para sugerir que no deben modificarse directamente
        self._x = x
        self._y = y
    
    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y
    
    def __str__(self):
        return f"Punto({self.x}, {self.y})"


# Crea un objeto de la clase Punto
p = Punto(3,4)

# Acceso a sus atributos
print(p.x)
print(p.y)

# Intentar modificar los atributos lanzará un error
#p.x = 10