# Estructura de datos que nos permite almacenar valores de diferentes
# tipos e incluso lista y otros diccionarios.

# La principal caracteristica de que los datos almacenan asociados a
# una clave de tal forma que se crea una asociacion de tipo clave:valor
# para cada elemento almacenado.

# Los elementos almacendos no estan ordenados. El orden es indiferente
# a la hora de almancenar informacion en un diccionario.

# Creacion de un diccionario
miDiccionario = {"Argentina":"Buenos Aires","Uruguay":"Montevideo","Brasil":"Sao Pablo"}

# Agregar un elemento al diccionario
miDiccionario["Chile"] = "Santiago"

# Salida de todo el diccionario
print(miDiccionario)

# Salida de un clave:valor especifico
print(miDiccionario["Argentina"])

# Editar un valor de una clave
miDiccionario["Brasil"] = "Brasilia"
print(miDiccionario)

# Eliminar la pareja clave:valor
del miDiccionario["Chile"]
print(miDiccionario)

# Uso de una tupla para usarla como claves
miTupla = ("Argentina","Uruguay","Brasil")

miDiccionario2 = {miTupla[0]:"Buenos Aires", miTupla[1]:"Montevideo",
				miTupla[2]:"Sao Pablo"}

# Uso de conversion de tipo dicc a string para concatenar
print("Con tupla " + str(miDiccionario2))


# Uso de diccionario dentro de otro
miSuperDiccionario = {23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago",
					"Anillos":{"Temporadas":[1991,1992,1993,1996,1997,1998]}}
print(miSuperDiccionario)
print(miSuperDiccionario.keys())
print(miSuperDiccionario.values())
print(len(miSuperDiccionario))