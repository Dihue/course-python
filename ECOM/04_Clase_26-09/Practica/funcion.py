# Funciones --> retorna valor / Procedimiento --> no retorna un valor

def saludo():
    print("Hola!")

# Devuelve lo que hace la funcióm
# saludo()

# x = saludo()
# Muestra el return que tiene implicito las funciones
# en este caso es NONE
# print(x)

# Funcion con parámetros/argumentos
def saludar(nombre, apellido, domicilio=None):

    print(f"Nombre: {nombre}, Apellido: {apellido}")
    # Verifica que el parámetro no sea None
    if domicilio:
        print(f"vive en {domicilio}")

# x = saludar("Dihue","De Cuadra")
# x = saludar(apellido="De Cuadra",nombre="Dihue")
# x = saludar(apellido="De Cuadra",nombre="Dihue", domicilio="calle 123")


# Funcion con argumentos posicionales
def sumar(*args):
    print(args.__class__.__name__)
    return None

suma = sumar(4,5,6,7)
# print(f"Suma: {suma}")

def sumando(*todos_los_argumentos):
    suma = 0

    for num in todos_los_argumentos:
        # Acumulador
        suma += num
    
    return suma

# suma = sumando(4,5,6,7)
# print(f"Suma: {suma}")

# Funcion con argumentos de palabras clave
# def saludar_2_args_palabras_clave(**kwargs)
def saludar_2(**todos_los_argumentos):

    # print(todos_los_argumentos)
    # print(todos_los_argumentos.__class__.__name__)

    # Al tratarse de un diccionario se puede usar el método GET
    # para darle un valor por defecto y evitar posibles errores
    # cuando no se tiene todos los argumentos
    print("Nombre: ",todos_los_argumentos["nombre"])
    print("Apellido: ",todos_los_argumentos.get("apellido", "-----"))


saludar_2(nombre="Dihue", apellido="Corazza")
print("==========================")
saludar_2(nombre="Dihue")