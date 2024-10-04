#! usr/bin/python

#Módulos importados
import sqlite3
import time
import os

#Conexión con Base de Datos Sqlite3
con = sqlite3.connect("agenda.db")
cursor = con.cursor()
#Comprueba si la tabla existe, en caso de no existir la crea
cursor.execute("""CREATE TABLE IF NOT EXISTS PERSONA (nombre TEXT, apellido TEXT, telefono TEXT, correo TEXT)""")

cursor.close()

#Declaración de las funciones

def limpiar():

	"""Limpia la pantalla"""

	if os.name == "posix":
		os.system("clear")
	elif os.name == ("ce", "nt", "dos"):
		os.system("cls")

def agregar():
	"""Agrega un nuevo contacto a la Agenda"""

	print("Agregar contacto")
	print("----------------")

	con = sqlite3.connect("agenda.db")
	cursor = con.cursor()

	nombre = input("Ingrese Nombre: ")
	apellido = input("Ingrese Apellido: ")
	telefono = input("Ingrese Teléfono: ")
	correo = input("Ingrese Correo Electrónico: ")

	cursor.execute("INSERT INTO  PERSONA (nombre, apellido, telefono, correo) VALUES ('%s','%s','%s','%s')"%(nombre,apellido,telefono,correo))

	con.commit()

	print("Los datos fueron agregados correctamente")

	cursor.close()
	time.sleep(2)
	main()

def listar():
	"""Devuelve todos los contactos de la agenda"""

	print ("Lista de contactos")
	print ("------------------")

	con = sqlite3.connect("agenda.db")
	cursor = con.cursor()

	cursor.execute("SELECT * FROM PERSONA")
	resultado = cursor.fetchall()

	for i in resultado:
		print("%s %s %s %s" % (i[0],i[1],i[2],i[3]))

	cursor.close()

	print("")
	input("Presione una tecla para continuar...")

	main()

def buscar():

	"""Busca un contacto en la agenda y lo lista"""

	print("Buscar contacto")
	print("---------------")

	con = sqlite3.connect("agenda.db")
	cursor = con.cursor()

	buscar = input("Ingrese Nombre a buscar: ")

	cursor.execute ("SELECT * FROM PERSONA WHERE nombre = '%s'" %(buscar))

	x = cursor.fetchall()

	print("")

	for i in x:
		print("Nombre:", i[0])
		print("Apellido:", i[1])
		print("Telefono:", i[2])
		print("Correo:", i[3])

	cursor.close()

	print("")
	input("Presione una tecla para continuar...")

	main()

def eliminar():

	"""Elimina un contacto de la Agenda"""

	print("Eliminar contacto")
	print("-----------------")

	con = sqlite3.connect("agenda.db")
	cursor = con.cursor()

	eliminar = input ("Ingrese Nombre de contacto a eliminar: ")

	cursor.execute("DELETE FROM datos WHERE nombre='%s'"%(eliminar))

	con.commit()

	cursor.close()

	print("Se ha eliminado el contacto correctamente...")
	input("Presione una tecla para continuar...")
	main()


def main():
	"""Función principal de la Agenda"""

	limpiar()

	print("-----------------------------------------")
	print("AGENDA DE CONTACTOS - MENÚ")
	print("-----------------------------------------")
	print("[1] Ingresar Contacto \n [2] Listar Contactos \n [3] Buscar Contacto \n [4] Eliminar Contacto \n [0] Salir")
	print("-----------------------------------------")

	opcion = input("Ingresa una opción -> ")

	if opcion != "1" and opcion != "2" and opcion != "3" and opcion != "4" and opcion != "5" and opcion != "0":
		print("Opción incorrecta")
		input()
		main()
	elif opcion == "1":
		limpiar()
		agregar()
	elif opcion == "2":
		limpiar()
		listar()
	elif opcion == "3":
		limpiar()
		buscar()
	elif opcion == "4":
		limpiar()
		eliminar()
	elif  opcion == "0":
		print ("Gracias por usar la Agenda")
		print ("Cerrando programa...")
		time.sleep(3)
		exit()

main()