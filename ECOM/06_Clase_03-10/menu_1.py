def opcion1():
    print("esta es la opcion 1")
    print("presione enter para continuar")
    input()


def opcion2():
    print("esta es la opcion 2")
    print("presione enter para continuar")
    input()


MENU_PRINCIPAL = [
    {
        "nombre": "Opcion 1"
    },
    {
        "nombre": "Opcion 2"
    },
    {
        "nombre": "Salir"
    }
]


while True:
    print("Ingrese una de las siguientes opciones:")
    
    for indice, op_dict in enumerate(MENU_PRINCIPAL):
        print(f"{indice+1} - {op_dict['nombre']}")

    print("---------------------")
    opcion = input(">")
    if not opcion.isnumeric():
        print("solo valores numericos")
        continue
    print("esta tod bien")

    if opcion == "1":
        opcion1()
    elif opcion == "2":
        opcion2()
    elif opcion == "3":
        break
    else:
        print("error, dato incorrecto")

