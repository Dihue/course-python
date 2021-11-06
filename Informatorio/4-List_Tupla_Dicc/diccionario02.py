'''
Un programa que me permita cargar los datos de los alumnos del
info nombre, localidad y dni

Me permita agregar  la nota de los exámenes, teniendo en cuenta
que hay dos módulos y 3 notas para cada uno.

Debe tener un menú interactivo que permita:
	Mostrar el alumno con mayor promedio
	Mostrar todos los que aprobaron ambos módulos
	Dado el DNI de un alumno, me muestre sus notas.
'''

import operator

def menu():
	# funcion vista
    print("\n| -------------- MENU -------------- |")
    print("|--> 1: Agregar estudiante")
    print("|--> 2: Estudiante con mayor promedio")
    print("|--> 3: Todos los estudiante aprobados")
    print("|--> 4: Notas de un estudiante")
    print("|--> 5: Salir")
    return input("\n Indique opción elegida: ")


def agregar(alumnos):
	# funcion para ingresar los datos del estudiante
	print("\n|-> Ingresar datos:")
	dni = int(input(" DNI: "))
	nombre = input(" Nombre/s: ")
	localidad = input(" Localidad de residencia: ")

	notasPW = []
	notasBD = []
	
	print("\n|-> Indique las notas de Programación Web:")
	for pw in range(3):
		nota = int(input(f" Nota nº {pw+1} = "))
		notasPW.append(nota)
	
	print("\n|-> Indique las notas de Base de Datos:")
	for bd in range(3):
		nota = int(input(f" Nota nº {bd+1} = "))
		notasBD.append(nota)

	alumnos[dni] = {"nombre": nombre, "localidad": localidad, "notasPW": notasPW, "notasBD": notasBD}
	
	return alumnos


def mayor_promedio(alumnos):
	# funcion que muestra el estudiante con mayor promedio
	lista_promedio = {}

	for k in alumnos.keys():
		
		suma = 0
		for i in range(3):
			suma = suma + alumnos[k]["notasPW"][i] + alumnos[k]["notasBD"][i]
			promedio = suma / 6

			lista_promedio[k] = promedio

	mayor_promedio = max(lista_promedio, key=lista_promedio.get)

	print("\nAlumno/a " + alumnos[mayor_promedio]["nombre"] + " tiene un promedio de " + str(round(lista_promedio[mayor_promedio],2)))


def aprobados(alumnos):
	# funcion para mostras a todos los estudiantes aprobados
    lista_promedio = {}

    for k in alumnos.keys():
    	suma_PW = 0
    	suma_BD = 0

    	for i in  range(3):
    		suma_PW = suma_PW + alumnos[k]["notasPW"][i]
    		promedio_PW = suma_PW / 3

    		if promedio_PW >= 6:
    			lista_promedio[k] = promedio_PW

    	for i in  range(3):
    		suma_BD = suma_BD + alumnos[k]["notasBD"][i]
    		promedio_BD = suma_BD / 3

    		if promedio_BD >= 6:
    			lista_promedio[k] = promedio_BD

    print("\n|-> Estudiantes aprobados:")
    for k,v in lista_promedio.items():
    	print(f"DNI: {k}, promedio: {round(v,2)}")


def mostrar_notas(alumnos):
	# funcion solo para mostrar las notas de un estudiante mediante su DNI
	dato = int(input("\n|-> Ingrese DNI del estudiante: "))
	
	print(" Programación Web:", alumnos[dato]["notasPW"])
	print(" Base de Datos: ", alumnos[dato]["notasBD"])


def main():
	# funcion controller
    alumnos = {}
    # alumons pre-cargados de ejemplo
    alumnos[1111] = {"nombre": "Dihue", "localidad": "SP", "notasPW": [10,7,7], "notasBD": [8,10,7]}
    alumnos[2222] = {"nombre": "Virginia", "localidad": "Ctes", "notasPW": [8,8,8], "notasBD": [8,8,8]}
    alumnos[3333] = {"nombre": "Damian", "localidad": "Resis", "notasPW": [3,4,5], "notasBD": [4,5,6]}

    while True:
        op = menu()
        if op == "1":
            alumnos = agregar(alumnos)
            # print de control
            print(alumnos)

        elif op == "2":
            alumnos = mayor_promedio(alumnos)

        elif op == "3":
        	alumnos = aprobados(alumnos)

        elif op == "4":
            alumnos = mostrar_notas(alumnos)

        else:
            break
        input("\n|-> Enter para continuar")

main()


'''

alumnos = {}

alumnos[1234] = {"nombre": "Dihue", "localidad": "SP", "notasPW": [10,7,7], "notasBD": [8,10,7]}
alumnos[4321] = {"nombre": "Damian", "localidad": "SP", "notasPW": [2,2,2], "notasBD": [2,2,2]}
alumnos[1111] = {"nombre": "Virginia", "localidad": "Ctes", "notasPW": [8,8,8], "notasBD": [8,8,8]}

#print(alumnos)
#print(alumnos.keys())
#print(alumnos.values())
#print(alumnos[1234]["notasPW"])


lista_promedio = {}

for k in alumnos.keys():
	
	print("\nKey: ",k)
	suma = 0
	for i in range(3):
		suma = suma + alumnos[k]["notasPW"][i] + alumnos[k]["notasBD"][i]
		print(suma)
		promedio = suma / 6
		lista_promedio[k] = promedio
	print("Promedio: ",promedio)

mayor_promedio = max(lista_promedio, key=lista_promedio.get)

print(lista_promedio)

print("\nAlumno/a " + alumnos[mayor_promedio]["nombre"] + " tiene un promedio de " + str(round(lista_promedio[mayor_promedio],2)))
cont = 1

	while cont <= 2:
		opcion = input("\n¿Desea agregar las notas del alumno?\n|-> 1: Si\n|-> 2: No\n\n Indique opción: ")

		if opcion == '1':
		if opcion == '1':
			modulo = input("\nLas notas son de:\n|-> 1: Programación Web\n|-> 2: Base de Datos\n\n Indique opción: ")
			
			if modulo == '1':
				for pw in range(3):
					nota = int(input(f"Ingresar nota nº {pw+1} = "))
					notasPW.append(nota)
				cont += 1

			elif modulo == '2':
				for bd in range(3):
					nota = int(input(f"Ingresar nota nº {bd+1} = "))
					notasBD.append(nota)
				cont += 1


'''