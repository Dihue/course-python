import random

def generador_numeros():
    return random.randint(1,100)

print("\nBienvenido al generador de números aleatorios")

respuesta = input("Ingrese S para iniciar o N para terminar: ")

while respuesta.upper() == 'S':
    numero = generador_numeros()
    print(f"El número generado es: {numero}")

    respuesta = input("¿Desea generar otro número? (S/N)\n")

print("\nGracias por jugar")