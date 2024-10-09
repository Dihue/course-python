def opcion1():
    print("esta es la opcion 1")
    print("presione enter para continuar")
    input()


def opcion2():
    print("esta es la opcion 2")
    print("presione enter para continuar")
    input()


def salir():
    print("chau!")

MENU_PRINCIPAL = {
    1: {
        "nombre": "Opcion 1",
        "metodo": opcion1
    },
    2: {
        "nombre": "Opcion 2",
        "metodo": opcion2
    },
    3: {
        "nombre": "Salir",
        "metodo": salir
    }
}   



while True:
    print("Ingrese una de las siguientes opciones:")
    
    for indice, op_dict in MENU_PRINCIPAL.items():
        print(f"{indice} - {op_dict['nombre']}")

    print("---------------------")
    opcion = input(">")
    if not opcion.isnumeric():
        print("solo valores numericos")
        continue
    
    MENU_PRINCIPAL.get(int(opcion))["metodo"]()
    

    """
    if opcion == "1":
        opcion1()
    elif opcion == "2":
        opcion2()
    elif opcion == "3":
        break
    else:
        print("error, dato incorrecto")
    """

