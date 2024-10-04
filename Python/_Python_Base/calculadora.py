def suma(a, b):
    resultado = a + b
    print(f"\nEl resultado de la suma es {resultado}")

def resta(a, b):
    resultado = a - b
    print(f"\nEl resultado de la resta es {resultado}")

def multiplicar(a, b):
    resultado = a * b
    print(f"\nEl resultado de la multiplicación es {resultado}")

def dividir(a, b):
    if b == 0:
        print("No se puede realizar división por cero")
    else:
        resultado = a / b
        print(f"\nEl resultado de la división es {resultado}")

def menu():
    print("\n- - - Calculadora - - -")
    print("Eliga una opción")
    print("1 - Suma")
    print("2 - Resta")
    print("3 - Multiplicación")
    print("4 - División\n")
    opcion = int(input("Opción:\n"))
    return opcion

def calculadora():
    selector = menu()

    num1 = int(input("Ingrese primer número: "))
    num2 = int(input("Ingrese segundo número: "))
    
    if selector == 1:
        suma(num1, num2)
    elif selector == 2:
        resta(num1, num2)
    elif selector == 3:
        multiplicar(num1, num2)
    elif selector == 4:
        dividir(num1, num2)
    else:
        print("Opción incorrecta")

calculadora()
