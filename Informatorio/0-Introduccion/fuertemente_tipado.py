# Ya que no se permiten violaciones de los tipos de datos, es decir,
# dado el valor de una variable de un tipo concreto, no se puede usar
# como si fuera de otro tipo distinto a menos que se haga una conversión.

# Por ejemplo:
# Si asigno estos valores a las variables x e y:

X = 2
Y = "5"

#Para poder sumarlos debo primero convertir explícitamente a la variable
# y en un entero.

R = X + int(Y)
print(R)