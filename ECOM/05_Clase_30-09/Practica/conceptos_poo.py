# Pilares de la POO
#? 1) Abstracción
#? 2) Encapsulamiento
#? 3) Herencia
#? 4) Polimorfismo

#* Componentes del Objeto:
#? Atributos, características
#? Métodos, servicios
#? Identificador


class Coche:
    # Coche: marca, modelo (atributos)

    # Constructor
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    # Métodos
    def conducir(self):
        # print(f"Conduciendo el {self.marca} {self.modelo}")
        return f"Conduciendo el {self.marca} {self.modelo}"

# Instancia de la clase
coche1 = Coche(marca="Ford", modelo="Focus")

print(coche1.marca)
print(coche1.modelo)
print(coche1.conducir())