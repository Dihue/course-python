from triangulo import Triangulo


t = Triangulo(2,2,3)
"""
lado_a_mostrar = "lado3"
lado3 = getattr(t, lado_a_mostrar)
print("lado3", lado3)

setattr(t, lado_a_mostrar, 55)

lado3 = getattr(t, lado_a_mostrar)
print("lado3", lado3)
"""

lado_a_mostrar = "lado4"
lado3 = getattr(t, lado_a_mostrar, "no existe")
print("lado3", lado3)

