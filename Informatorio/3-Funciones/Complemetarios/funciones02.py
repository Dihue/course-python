'''
Ejercicio 2: Tarifa del taxi

En una jurisdicción particular, las tarifas de taxi consisten
en una tarifa base de $40.00, más $15.00 por cada 140 metros
recorridos. Escriba una función que tome la distancia recorrida
(en kilómetros) como su único parámetro y devuelva la tarifa
total como su único resultado. Escriba un programa principal
que use la función.

Sugerencia: Utilice constantes para presentar la base y la por-
ción variable de las tarifas así el programa podrá actualizar
fácilmente cuando las tasas aumentan.
'''

BASE = 40.00
TARIFA_METROS = 15.00 * 0.140

def tarifaTotal(distancia):
	'''funcion para el calculo total del costo del recorrido de un taxi'''
	total = BASE + TARIFA_METROS * distancia

	return total

distancia = float(input("\nIndique la distancia recorrida: "))

print(tarifaTotal(distancia))