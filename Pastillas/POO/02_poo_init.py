class Coche:
    # constructor de estado inicial
    def __init__(self):
        self.largoChasis = 250
        self.anchoChasis = 120
        # atributo encapsulado
        self.__ruedas = 4
        self.encendido = False

    # comportamientos de la clase(metodos)
    def arrancar(self,arrancamos):
        self.encendido = arrancamos

        if (self.encendido):
            chequeo = self.__chequeo_interno()

        if (self.encendido and chequeo):
            return "Coche en marcha"
        elif (self.encendido and chequeo==False):
            return "Algo anda mal en el chequeo, no podemos arrancar"
        else:
            return "Coche apagado"

    def estado(self):
        print(f"Tiene {self.__ruedas} ruedas")

    # Metodo encapsulado
    def __chequeo_interno(self):
        print("Realizando chequeo interno")

        self.gasolina = "ok"
        self.aceite = "ok"
        self.puertas = "cerradas"

        if (self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):
            return True
        else:
            return False

        
print("\n----- Primer objeto o instancia -----\n")
# instanciar la clase
miCoche = Coche()

# salida por pantalla
#print(f"Ancho coche: {miCoche.anchoChasis}")
#print(f"Largo coche: {miCoche.largoChasis}")

print(miCoche.arrancar(True))
miCoche.estado()

print("\n----- Segundo objeto o instancia -----\n")
# instanciar la clase
miCoche2 = Coche()

#print(f"Ancho coche: {miCoche2.anchoChasis}")
#print(f"Largo coche: {miCoche2.largoChasis}")

print(miCoche2.arrancar(False))
# no se modifica por el encapsulamiento
#miCoche2.ruedas = 2
miCoche2.estado()