def opcion1():
    print("Esta es la opción 1")
    print("Presione enter para continuar")
    input()


def opcion2():
    print("Esta es la opción 2")
    print("Presione enter para continuar")
    input()

def salir():
    print("Saliendo...")


MENU_PRINCIPAL = {
    1: {
        "nombre": "Opción 1",
        "metodo": opcion1
    },
    2: {
        "nombre": "Opción 2",
        "metodo": opcion2
    },
    3: {
        "nombre": "Salir",
        "metodo": salir
    }
}


while True:
    print("- - - - - - - - - - - - - - - - - - - - ")
    print("Ingrese una de las siguientes opciones:")
    # Con indice y op desempaqueto el diccionario del menu
    for indice, op_dict in MENU_PRINCIPAL.items():
        print(f"-> {indice} - {op_dict['nombre']}")
    print("- - - - - - - - - - - - - - - - - - - - ")
    opcion = input("-> ")

    if not opcion.isnumeric():
        print("\nIngrese sólo valores numéricos\n")
        continue
    print("\nOpción correcta\n")

    MENU_PRINCIPAL.get(int(opcion))["metodo"]()
