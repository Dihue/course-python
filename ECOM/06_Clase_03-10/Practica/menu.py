def opcion1():
    print("Esta es la opción 1")
    print("Presione enter para continuar")
    input()


def opcion2():
    print("Esta es la opción 2")
    print("Presione enter para continuar")
    input()


MENU_PRINCIPAL = [
    {
        "Nombre": "Opción 1"
    },
    {
        "Nombre": "Opción 2"
    },
    {
        "Nombre": "Salir"
    }
]


while True:
    print("- - - - - - - - - - - - - - - - - - - - ")
    print("Ingrese una de las siguientes opciones:")
    # Con indice y op desempaqueto el diccionario del menu
    for indice, op_dict in enumerate(MENU_PRINCIPAL):
        print(f"-> {indice + 1} - {op_dict["Nombre"]}")
    print("- - - - - - - - - - - - - - - - - - - - ")
    opcion = input("-> ")

    if not opcion.isnumeric():
        print("\nIngrese sólo valores numéricos\n")
        continue
    print("\nOpción correcta\n")

    if opcion == "1":
        opcion1()
    elif opcion == "2":
        opcion2()
    elif opcion == "3":
        break
    else:
        print("\n< - Error, dato incorrecto - >\n")


# Muestra una tupla con la numerancion o indice de los
# elementos junto con cada elemento
# print(list(enumerate(MENU_PRINCIPAL)))