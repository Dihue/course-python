# INSTANCIAS DE CLASE
'''
Para entender bien los objetos, debemos tener claras dos cuestiones fundamentales:

¿Cuando y donde existen los objetos?

Puede parecer trivial, pero es importante tener claro que los objetos "existen" so-
lo durante la ejecucion del programa y se almacenan en la memoria del sistema ope-
rativo, es decir, mientras las clases estan ahi en el codigo haciendo su papel de
instrucciiones, los objetos no existen hasta que el programa se ejecuta y se crean
en la memoria.

Este proceso de "crear" los objetos en la memoria se denomina INSTANCIACION y para
realizarlo es tan facil como llamar a la clase como si fuera una funcion:
'''

class Galleta:
    pass

una_galleta = Galleta()
otra_galleta = Galleta()

'''
Demostrar que cada galleta existe como "entes independientes" dentro de la memoria,
es tan sencillo como imprimirlas por pantalla
'''

print(una_galleta)
print(otra_galleta)

'''
Cada instancia tiene su propia referencia, demostrando que estan en lugares distin-
tos de la memoria. En cambio la clase no tiene una referencia porque es solo un gui-
on de instrucciones.
'''

print()
print(Galleta)

'''
Es posible consultar la clase de un objeto con la funcion type(), pero tambien se
puede consultar a traves de su atributo especial class:
'''

print(type(una_galleta))
print(una_galleta.__class__)
print()

'''
A su vez, las clases tienen un atributo especial name que nos devuelve su nombre en
forma de cadena sin adornos:
'''

print(Galleta.__name__)
print(type(una_galleta).__name__)
print(una_galleta.__class__.__name__)