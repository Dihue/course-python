# Creo una estructura para los clientes

class Clientes:

    def __init__(self,dni,nombre,apellido):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self) -> str:
        return '{} {}'.format(self.nombre,self.apellido)