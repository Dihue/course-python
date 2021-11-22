'''
Crear una clase Tiempo, con atributos hora, minuto y segundo, que pueda ser
instanciada indicando: los tres atributos, sólo la hora y minuto,o sólo la
hora. Crear además los métodos necesarios para modificar la hora en cualquier
momento de forma manual. Mantenga la integridad de los datos en todo momento
definiendo de tipo “private”. Crear una clase prueba_tiempo que prueba una hora
concreta y la modifique a su gusto mostrándola por pantalla.
'''

from datetime import datetime
import random


class Tiempo:

    def __init__(self,hora,minutos=0,segundos=0):
        self.__hora = hora
        self.__minutos = minutos
        self.__segundos = segundos

    def getHora(self):
        return self.__hora
    def setHora(self,nuevaHora):
        self.__hora = nuevaHora

    def getMinutos(self):
        return self.__minutos
    def setMinutos(self,nuevoMinuto):
        self.__minutos = nuevoMinuto

    def getSegundos(self):
        return self.__segundos
    def setSegundos(self, nuevoSegundo):
        self.__segundos = nuevoSegundo

    def __str__(self):
        return f"Hora: {self.__hora}:{self.__minutos}:{self.__segundos}"

class Prueba_tiempo:
    hora_oficial = datetime.now().strftime("%H:%M:%S")

    def __init__(self,hora,minutos,segundos):
        self.__hora = hora
        self.__minutos = minutos
        self.__segundos = segundos

    def getHora(self):
        return self.__hora
    def setHora(self,nuevaHora):
        self.__hora = nuevaHora

    def getMinutos(self):
        return self.__minutos
    def setMinutos(self,nuevoMinuto):
        self.__minutos = nuevoMinuto

    def getSegundos(self):
        return self.__segundos
    def setSegundos(self, nuevoSegundo):
        self.__segundos = nuevoSegundo

    def __str__(self):
        return f"Hora ofiacial: {self.hora_oficial}\
            \n Hora: {self.__hora}:{self.__minutos}:{self.__segundos}"


hs = int(input("Hora:"))
mn = int(input("Minutos:"))
seg = int(input("Segundos:"))

hs1 = random.randint(1,12)
mn1 = random.randint(1,59)
seg1 = random.randint(1,59)

t1 = Prueba_tiempo(hs,mn,seg)
t2 = Tiempo(hs1)
t3 = Tiempo(hs1,mn1)
t4 = Tiempo(hs1,mn1,seg1)

print("\nPrueba de tiempo\n",t1)
print("\nTiempo\n",t2)
print(t3)
print(t4)

#print(datetime.now().strftime(f'{hs}:{mn}:{seg}'))