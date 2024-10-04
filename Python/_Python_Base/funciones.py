def saludar_print():
    ''' Esta función imprime por terminal el mensaje
        Hola Mundo
    '''
    print("Hola Mundo")

def saludar_return():
    ''' Esta función devuelve el mensaje
        Hola Mundo
    '''
    return "Hola Mundo"


## Llamado de la función
#saludar_print()
#print(saludar_return())

def sumar(num1, num2):
    return num1 + num2

num1 = int(input("Ingrese primer número:\n"))
num2 = int(input("Ingrese segundo número:\n"))

print(sumar(num1,num2))

def super(**kwargs):
    return kwargs