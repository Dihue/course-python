'''# Listas [] indice comienza en 0

ejemplo = [12,23,34,45,56]

edades = list()

op = "si"

while op == "si":
    edad = int(input("Ingresar edad alumno/a: "))
    edades.append(edad)

    op = input("Desea cargar otro? si - no ")

for e in edades:
    print(f"Edad-->{e}")
'''
# Tuplas

alumnos = list()

op = 'si'

while op == 'si':
    nombre = input("Ingresar nombre alumno/a: ")
    edad = int(input("Ingresar edad del alumno/a: "))

    alumnos.append( (nombre,edad) )
    op = input("Desea cargar otro? si - no ")

for e in alumnos:
    print(f"Alumnos-->{e[0]} Edad-->{e[1]}\n")