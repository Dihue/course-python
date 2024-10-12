from triangulo3 import Triangulo

t = Triangulo(2,4,1)

# Método que toma atributos de las clases de forma dinámica
# getattr necesita del objeto y del nombre del atributo
lado_a_mostrar = "lado3"
lado3 = getattr(t, lado_a_mostrar)
print("Lado 3:", lado3)

# Método que cambia el valor de un atributo de la clase
setattr(t, lado_a_mostrar, 12)

lado3 = getattr(t, lado_a_mostrar)
print("Lado 3:", lado3)

# Se asigna un valor por default en caso de no encontrar
# el nombre del atributo de la clase
lado_a_mostrar = "lado4"
lado3 = getattr(t, lado_a_mostrar, "No existe")
print("Lado 3:", lado3)