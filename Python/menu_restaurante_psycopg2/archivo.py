import psycopg2 # type: ignore

def crear_basededatos():
  # Función que crea la base de datos menu_restaurante.db
	conexion = psycopg2.connect(database = "menu_restaurante.db",
															user = "root",
															host= 'localhost',
															password = "rootpass",
															port = 3306)
	cursor = conexion.cursor()

	# Creamos la tabla Categoría
	try:
		cursor.execute('''CREATE TABLE categoria(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre VARCHAR(100) UNIQUE NOT NULL)''')

	except psycopg2.OperationalError: # Si hay un error
		print("La tabla de Categorías ya existe.")

	else: # Si todo funciona correctamente
		print("La tabla de Categorías se ha creado correctamente.")

	# Creamos la tabla Plato
	try:

		cursor.execute('''CREATE TABLE plato(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre VARCHAR(100) UNIQUE NOT NULL,
                categoria_id INTEGER NOT NULL,
                FOREIGN KEY(categoria_id) REFERENCES categoria(id))''')
  # La línea anterior indica un tipo de clave especial (foránea), por la cual se crea una relación entre la categoría de un plato con el registro de categorías.


	except psycopg2.OperationalError:
		print("La tabla de Platos ya existe.")
	else:
		print("La tabla de Platos se ha creado correctamente.")

		conexion.commit()
		cursor.close()
		conexion.close() # Cerramos la conexión
#-------------------------

def agregar_categoria(): # Función que  pide al usuario un nombre de categoría y se encargue de crear la categoría en la base de datos.
	categoria_usuario= input("¿Nombre de la nueva categoría?\n> ")

	conexion = psycopg2(database = "menu_restaurante.db",
															user = "root",
															host= 'localhost',
															password = "rootpass",
															port = 3306)
	cursor = conexion.cursor()

	try:
		cursor.execute("INSERT INTO categoria VALUES(null,'{}')".format(categoria_usuario)) # null para el campo autoincremental.
	except psycopg2.OperationalError:
		print("La categoría '{}' ya existe.".format(categoria_usuario))
	else:
		print("La categoría '{}' se ha creado correctamente.".format(categoria_usuario))


	conexion.commit() # Confirmamos cambios
	cursor.close()
	conexion.close() # Cerramos la conexión
#-------------------------

def agregar_plato(): # Función que muestra al usuario las categorías disponibles y le permite escoger una.

# Después pide introducir el nombre del plato y lo añade a la base de datos.
# La categoría del plato debe coincidir con el id de la categoría y el nombre del plato no puede repetirse.

	conexion = psycopg2.connect(database = "menu_restaurante.db",
															user = "root",
															host= 'localhost',
															password = "rootpass",
															port = 3306)
	cursor = conexion.cursor()


	categorias=cursor.execute("SELECT * FROM categoria").fetchall() # Consultamos las categorías de la base de datos.
	print("Selecciona una categoría para añadir el plato: ")
	for categoria in categorias: # Recorremos las categorías
		print("[{}]{}".format(categoria[0],categoria[1])) # Mostramos el id y nombre de la categoría

	categoria_usuario=int(input("> ")) # Guardamos en una variable de tipo entero, la categoría que introduce el usuario.
	plato_usuario= input("¿Nombre del plato?\n> ")


	try:
		cursor.execute("INSERT INTO plato VALUES(null,'{}','{}')".format(plato_usuario,categoria_usuario)) # null para el campo autoincremental.
	except psycopg2.OperationalError:
		print("El plato '{}' ya existe.".format(plato_usuario))
	else:
		print("El plato '{}' se ha creado correctamente.".format(plato_usuario))


	conexion.commit() # Confirmamos cambios
	cursor.close()
	conexion.close() # Cerramos la conexión
#-------------------------

def mostrar_menu(): # Función que muestra el menú con todos los platos de forma ordenada: los primeros, los segundos y los postres.
	conexion = psycopg2.connect(database = "menu_restaurante.db",
															user = "root",
															host= 'localhost',
															password = "rootpass",
															port = 3306)
	cursor = conexion.cursor()

	categorias = cursor.execute("SELECT * FROM categoria").fetchall() # Consultamos las categorías de la base de datos.
	for categoria in categorias:
		print(categoria[1]) # Mostramos el nombre de la categoría.

		# Consultamos todos los platos en la tabla plato, cuyo id (categoria_id) coincida con el id de la tabla categoria.
		platos = cursor.execute("SELECT * FROM plato WHERE categoria_id={}".format(categoria[0])).fetchall()
		for plato in platos:
			print("\t{}".format(plato[1])) # Mostramos todos los platos de la categoría, y repetimos el bucle para la siguiente categoría.

		conexion.commit()
		cursor.close()
		conexion.close() # Cerramos la conexión

#-------------------------

# Creamos la base de datos
crear_basededatos()

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

