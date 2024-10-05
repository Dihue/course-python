# Funciones --> retorna valor / Procedimiento --> no retorna un valor

def saludar(nombre, apellido, domicilio=None):

    print(f"Nombre: {nombre}, Apellido: {apellido}")

    if domicilio:
        print(f"vive en {domicilio}")

# x = saludar("Dihue","De Cuadra")
# x = saludar(apellido="De Cuadra",nombre="Dihue")
# x = saludar(apellido="De Cuadra",nombre="Dihue", domicilio="calle 123")

# def sumar(*args)
# funcion con argumentos posicionales
def sumar(*todos_los_argumentos):
    suma = 0

    for num in todos_los_argumentos:
        suma += num
    
    return suma

suma = sumar(4,5,6,7)
# print(f"Suma: {suma}")
