"""
Las variables son elementos que nos permiter guardar un dato
para que pueda ser accedido facilmente, manipulando y trans-
formado a lo largo de un programa.

	Manejor de Varibles

> Para definir una variable basta con nombrarla y definir su
  valor.

> Para crear y darle valores a nuevas variables, utilizamos
  la operacion de asignacion (=).

> Para modificar el valor de una variable, basta con asignar-
  le un nuevo valor luego de definirla.

> Se puede asignar a una variable un valor literal, una ex-
  presion, una llamada a un funcion o una combinacion de to-
  dos ellos.

	Nombres de Variables

> Pueden empezar con una letra o un guion bajo, por conven-
  cion no usamos mayusculas.

> Pueden contener letras, numeros y se puede usar el guion
  bajo (_).

> Son "case sentive", es decir, distingue si contiene mayus-
  culas o minusculas.

> No se puede utilizar palabras claves o reservadas de Python
  como nombres de variables.
"""

# Operadores Matematicos

suma = 20 + 30
print("El resultado de la suma es:", suma)

resta = 123 - 34
print("El resultado de la resta es:", resta)

division_flotante = 125 / 5
print("El resultado de la division es:", division_flotante)

division_entera = 125 // 5
print("El resultado de la division entera es:", division_entera)

mutiplicacion = 30 * 2
print("El resultado de la mutiplicacion es:", mutiplicacion)

modulo = 25 % 3
print("El resultado del modulo es:", modulo)

potencia = 5 ** 3
print("El resultado de la potencia es:", potencia)


# Operadores Logicos

a = True
b = True
c = False

# and
x = a and b
print("Resultado AND:", x)

# or
y = c or c
print("Resultado OR:", y)

# not
z = not a
print("Resultado NOT:", z)


# Operadores de String

concatenacion = "Hola " + "Mundo"
print("Resultado concatenacion:", concatenacion)

mutiplicacion = 'Hola ' * 3
print("Resultado mutiplicacion:", mutiplicacion)

mezcla = 'Hola ' * 3 + 'mundo'
print("Resultado mezcla:", mezcla)