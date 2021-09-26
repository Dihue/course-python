# Las tuplas son listas inmutables, no se pueden modificar despues
# de su creacion

# No permite añadir, eliminar, mover elementos
# Si permite extraer porciones
# Si permite comprobar si un elemento se encuentra dentro

# Utilidad o ventaja

# Más rapida
# Menos espacio
# Formatean Strings
# Pueden utilizarse como claves de un diccionario

# Creacion de una tupla
miTupla = ("Dihue",21,8,1991)

print(miTupla[1])

# Convertir una tupla en un lista
miLista = list(miTupla)

print(miLista)

# Convertir una lista en una tupla
miNuevaTupla = tuple(miLista)

print(miNuevaTupla)

# Buscar en la tupla
print("Dihue" in miTupla)

# Contar cuantas veces aparece un elemento
print(miTupla.count(8))

# Longitud de una tupla
print(len(miTupla))

# Tupla unitaria
miTuplaUni = ("Dihue",)

# Desempaquetado de una tupla
nombre, dia, mes, anio = miTupla
print(dia)
print(anio)