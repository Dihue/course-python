# Estructura de datos que nos permite almacenar gran cantidad de valores
# En Python las listas pueden guardar diferentes tipos de valores
# Se pueden expandir dinamicamente añadiendo nuevos elementos

# Creacion de una lista
miLista = ["Dihue",21,"Damian","Virginia",8.39,"Teresita"]

# Salida por pantalla de la lista completa
print(miLista)

# Agregar un elemento al final de la lista
miLista.append("Dizero")

# Agregar un elemento en un indice determinado
miLista.insert(2,"Didahue")

# Llamado por indice de la lista, de un elemento
print(miLista[1])
print(miLista[-1])

# Llamado de una porcion
print(miLista[0:3])

# Agregar multiples elementos
miLista.extend(["Sandra","Guada","Ana"])

print(miLista)

# Devuelve indice de un elemento
print(miLista.index("Dihue"))

# Encontrar un elemento dentro de la lista
print("Pepe" in miLista)

# Eliminar un elemento
miLista.remove("Ana")

# Eliminar el ultimo elemento de la lista
miLista.pop()

miLista2 = [1991,1987,2018]

miLista3 = miLista + miLista2

print(miLista3)