class Coche:
    # propiedades de la clase
    largoChasis = 250
    anchoChasis = 120
    ruedas = 4
    encendido = False

    # comportamientos de la clase(metodos)
    def arrancar(self,arrancamos):
        self.encendido = arrancamos

        if (self.encendido):
            return "Coche en marcha"
        else:
            return "Coche apagado"

    def estado(self):
        print(f"Tiene {self.ruedas} ruedas")
        

# instanciar la clase
miCoche = Coche()

# salida por pantalla
print(f"Ancho coche: {miCoche.anchoChasis}")
print(f"Largo coche: {miCoche.largoChasis}")

print(miCoche.arrancar(True))

miCoche.estado()

print("\n----- Segundo objeto o instancia -----\n")

miCoche2 = Coche()

print(f"Ancho coche: {miCoche2.anchoChasis}")
print(f"Largo coche: {miCoche2.largoChasis}")

print(miCoche2.arrancar(False))
miCoche2.estado()