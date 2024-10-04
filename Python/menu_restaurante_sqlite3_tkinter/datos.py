import sqlite3

ruta_base_datos = "D:/Users/Dihue/Desktop/Python/menu_restaurante_sqlite3_tkinter/menu_restaurante.db"

#Nos conectamos a la base de datos
conexion = sqlite3.connect(ruta_base_datos)
cursor = conexion.cursor()

#-------------------------

def agregar_categoria(): # Función que  pide al usuario un nombre de categoría y se encargue de crear la categoría en la base de datos.
	categoria_usuario= input("¿Nombre de la nueva categoría?\n> ")

	conexion = sqlite3.connect(ruta_base_datos)
	cursor = conexion.cursor()

	try:
		cursor.execute("INSERT INTO categoria VALUES(null,'{}')".format(categoria_usuario)) # null para el campo autoincremental.
	except sqlite3.OperationalError:
		print("La categoría '{}' ya existe.".format(categoria_usuario))
	else:
		print("La categoría '{}' se ha creado correctamente.".format(categoria_usuario))


	conexion.commit() # Confirmamos cambios
	conexion.close() # Cerramos la conexión

#-------------------------

def agregar_plato(): # Función que muestra al usuario las categorías disponibles y le permite escoger una.

# Después pide introducir el nombre del plato y lo añade a la base de datos.
# La categoría del plato debe coincidir con el id de la categoría y el nombre del plato no puede repetirse.

	conexion = sqlite3.connect(ruta_base_datos)
	cursor = conexion.cursor()


	categorias=cursor.execute("SELECT * FROM categoria").fetchall() # Consultamos las categorías de la base de datos.
	print("Selecciona una categoría para añadir el plato: ")
	for categoria in categorias: # Recorremos las categorías
		print("[{}]{}".format(categoria[0],categoria[1])) # Mostramos el id y nombre de la categoría

	categoria_usuario=int(input("> ")) # Guardamos en una variable de tipo entero, la categoría que introduce el usuario.
	plato_usuario= input("¿Nombre del plato?\n> ")


	try:
		cursor.execute("INSERT INTO plato VALUES(null,'{}','{}')".format(plato_usuario,categoria_usuario)) # null para el campo autoincremental.
	except sqlite3.OperationalError:
		print("El plato '{}' ya existe.".format(plato_usuario))
	else:
		print("El plato '{}' se ha creado correctamente.".format(plato_usuario))


	conexion.commit() # Confirmamos cambios
	conexion.close() # Cerramos la conexión

#-------------------------

def mostrar_menu(): # Función que muestra el menú con todos los platos de forma ordenada: los primeros, los segundos y los postres.
	conexion = sqlite3.connect(ruta_base_datos)
	cursor = conexion.cursor()

	categorias = cursor.execute("SELECT * FROM categoria").fetchall() # Consultamos las categorías de la base de datos.
	for categoria in categorias:
		print(categoria[1]) # Mostramos el nombre de la categoría.

		# Consultamos todos los platos en la tabla plato, cuyo id (categoria_id) coincida con el id de la tabla categoria.
		platos = cursor.execute("SELECT * FROM plato WHERE categoria_id={}".format(categoria[0])).fetchall()
		for plato in platos:
			print("\t{}".format(plato[1])) # Mostramos todos los platos de la categoría, y repetimos el bucle para la siguiente categoría.

	conexion.close()

#-------------------------

#Menú de opciones del programa
while True:
	print("\nBienvenido al gestor del restaurante!")
	opcion= input("\nIntroduce una opción:\n[1] Agregar una categoría\n[2] Agregar plato\n[3] Mostrar menú\n[4] Salir del programa\n\n> ")

	if opcion== "1":
		agregar_categoria()

	elif opcion == "2":
		agregar_plato()

	elif opcion == "3":
		mostrar_menu()

	elif opcion=="4":
		print("Hasta la próxima!")
		break # Rompemos la ejecución de bucle while para terminar el programa

	else:
		print("Opción Incorrecta")