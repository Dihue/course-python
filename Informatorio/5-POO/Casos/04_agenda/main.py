# Importar
from clases import Agenda, Contacto


def menu():
	# Funcion vista
	print("\n| -------------- MENU -------------- |")
	print("|--> 1: Agregar contacto")
	print("|--> 2: Todos los contacto")
	print("|--> 3: Buscar contacto")
	print("|--> 4: Editar contacto")
	print("|--> 5: Salir")
	return input("\n Indique opción elegida: ")


def main():
	# Funcion controller
	nombre_agrenda = input("|-> Definir nombre de la agenda: ")
	
	# Para crear la agenda debo definir su nombre primero
	miAgenda = Agenda(nombre_agrenda)
	
	# Print de control
	print(miAgenda.getNombreAg())

	while True:
		op = menu()
		if op == "1":
			# Parametros para el constructor
			nombre = input("\n|-> Nombre del contacto: ")
			telefono = int(input("|-> Número del contacto: "))
			email = input("|-> Email del contacto: ")

			# Constructor del contacto
			c = Contacto(nombre,telefono,email)

			# Llamado de la funcion agregar de la agenda
			miAgenda.agregar(c)
		
		elif op == "2":
			print("\n Lista de los contactos:")
			# Llamado de la funcion listar de la agenda
			miAgenda.listar()

		elif op == "3":
			print("\n Puede buscar por nombre, teléfono ó email:")
			
			# Parametro para la busqueda
			dato = input("\n|-> Indique valor de búsqueda: ")

			# Llamado de la funcion buscar de la agenda
			miAgenda.buscar(dato)

		elif op == "4":
			print("\n Para editar, debe buscar contacto por nombre, teléfono ó email:")
			
			# Parametro para la busqueda
			dato = input("\n|-> Indique valor de búsqueda: ")

			# Parametro para editar
			nuevo = input("\n|-> Indique valor nuevo: ")

			# Llamado de la funcion editar de la agenda
			miAgenda.editar(dato,nuevo)
			
		else:
			# Llamado de la funcion salir de la agenda
			miAgenda.salir()
			break

		input("\n|-> Enter para continuar")


main()




'''
En caso de que la creacion del contacto sea desde la clase

elif op == "0":
			# parametros para el contacto
			nombre = input(" Nombre del contacto: ")
			telefono = int(input(" Número del contacto: "))
			email = input(" Email del contacto: ")
			# creador del contacto
			miAgenda.agregarIn(nombre,telefono,email)

No implementado por la escalabilidad del problema(a mi parecer)
'''