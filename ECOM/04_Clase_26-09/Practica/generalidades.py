# Funciones lambda (comparación)
# Lambda se combina con funciones filter, reduce y maps
def sumar(x,y):
    return x+y

sumar1 = sumar(4,2)
# print("Suma 1: ", sumar1)


sumar_lambda = lambda x, y: x+y
sumar2 = sumar_lambda(4,2)
# print("Suma lambda: ", sumar2)


lista_valores = [2, 5, 6, 9]
print("Lista valores:", lista_valores)

nuevos_valores = []

for el in lista_valores:
    # multiplica cada valor de la lista y lo agrega a una nueva
    nuevos_valores.append(el*2)

print("Lista valores nuevos:", nuevos_valores)


# Lista por comprensión
nuevos_valores_2 = [num*2 for num in lista_valores]
print("Lista valores comprensión:", nuevos_valores_2)

# Condicional en una lista por comprension
nuevos_valores_3 = [num*2 for num in lista_valores if num>2]
print("Lista valores comprensión condicionada:", nuevos_valores_3)


# MAP (mapeo) aplica una funcion que recibe como
# argumento a todos los elemento de un lista iterable
nuevos_valores_map = map(lambda x: x * 2, lista_valores)
# Devuelve un objeto del tipo MAP
print("\nValores MAP:", nuevos_valores_map)
# Conversión o parseo
print("Valores MAP:", list(nuevos_valores_map))


# FILTER (filtra por una condición)
nuevos_valores_filter = list(filter(lambda z: z % 2 == 0, lista_valores))
print("\nValores FILTER:", nuevos_valores_filter)


# REDUCE (devuelve un único valor desde una lista iterable)
from functools import reduce

# Para este caso suma todos los elementos de lista iterable para
# devolver un único valor
valor = reduce(lambda x, y: x + y, lista_valores)
print("\nValor REDUCE:", valor)