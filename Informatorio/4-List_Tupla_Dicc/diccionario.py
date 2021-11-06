'''
Escribir un programa que implemente una agenda. En la agenda se podrán guardar nombres y números de teléfono. 
El programa nos dará el siguiente menú:

Añadir/modificar: Nos pide un nombre. Si el nombre se encuentra en la agenda, 
				  debe mostrar el teléfono y, opcionalmente, permitir modificarlo si no es correcto. 
  				  Si el nombre no se encuentra, debe permitir ingresar el teléfono correspondiente.
Buscar: Nos pide una cadena de caracteres, y nos muestras todos los contactos cuyos nombres comiencen por dicha cadena.
Borrar: Nos pide un nombre y si existe nos preguntará si queremos borrarlo de la agenda.
Listar: Nos muestra todos los contactos de la agenda.
'''


def agregar(agenda):
	nombre = input()
	numero = input()
	agenda[nombre] = numero
	return agenda

def modificar(agenda):
	nombre = input("Ingrese el nombre: \t")
	numero = int(input("Ingrese el número:\t"))
	agenda[nombre] = numero
	return agenda

def buscar(agenda):
	nombre = input("Nombre:\t")
	for k in agenda.keys():
		if k in agenda:
			print(f"El número de {k} es:{agenda[k]}")
		else:
			print("El nombre ingresado no se encuentra en la agenda!")

def borrar(agenda):
	#llamar a lista
	nombre = input("Nombre:\t")
	op = input("Quiere borrar su contacto?\t")
	if op == "si":
		del agenda[nombre]
		return agenda
	else:
		return agenda

def listar(agenda):
	for c,v in agenda.items():
		print (f"Nombre: {c} ------> Número: {v}")


def menu():
	#muestra por pantalla el menú para el usuario
	print("\nBienvenido a la agenda, ¿qué opción desea usar?\n")
	
	print(" -> 1 - Agregar contacto")
	print(" -> 2 - Modificar contacto")
	print(" -> 3 - Buscar contacto")
	print(" -> 4 - Borrar contacto")
	print(" -> 5 - Listar contactos")
	print(" -> 0 - Salir")

	return input("\nNúmero de opción: ")


def main():
	agenda = {}

	while True:
		opcion = menu()
		if opcion == "1":
			agenda = agregar(agenda)
		elif opcion == "2":
			agenda = modificar(agenda)
		elif opcion == "3":
			buscar(agenda)
		elif opcion == "4":
			agenda = borrar(agenda)
		elif opcion == "5":
			listar(agenda)
		else:
			break
		input("\nPresione Enter para continuar ")


main()