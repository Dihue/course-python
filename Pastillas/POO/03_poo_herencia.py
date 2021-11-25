class Vehiculos:

    def __init__(self,marca,modelo):
        self.__marca = marca
        self.__modelo = modelo
        self.__enmarcha = False
        self.__acelera = False
        self.__frena = False

    def arrancar(self):
        self.__enmarcha = True
    
    def acelerar(self):
        self.__acelera = True
    
    def frenar(self):
        self.__frena = True

    def estado(self):
        print(f"\n Marca: {self.__marca}\
            \n Modelo: {self.__modelo}\
            \n En marcha: {self.__enmarcha}\
            \n Acelerando: {self.__acelera}\
            \n Frenando: {self.__frena}")


class Moto(Vehiculos):
    pass


# Instancias
moto = Moto("Honda","CRB")

# Llamadas
moto.estado()