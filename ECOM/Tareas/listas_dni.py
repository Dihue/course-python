'''
Dado una lista de DNI de tipo String, validar el formato y obtener dos listas:
    1)  Una de las listas de DNI con formato válido
    2)  Una lista de DNI con formato inválido

Consideraciones para validar un DNI:
    -   Longitud: rango entre 7 y 8
    -   No deben tener caracteres especiales
    -   Todos los caracteres deben ser un dígito
    -   Otras consideraciones que sean necesarias

Entrada: ["12312312","12.123.32","00123456654","no se mi dni"]
Salida:     Lista1[]
            Lista2[]
'''

LONG_MIN_DNI = 7
LONG_MAX_DNI = 8

lista_dni = ["123456","no se","1234567"," ","12.123.12","12345678","123456789","s/num"]
lista_dni_valido = []
lista_dni_invalido = []


for dni in lista_dni:
    # validación para solo dígitos y longitud entre 7 y 8 dígitos
    if dni.isdigit() and len(dni) >= LONG_MIN_DNI and len(dni) <= LONG_MAX_DNI:
        lista_dni_valido.append(dni)
    else:
        lista_dni_invalido.append(dni)

print("\nLista de DNI válidos: ")
for dni in lista_dni_valido:
    print(dni, end=" ")

print("\n\nLista de DNI inválidos: ")
for dni in lista_dni_invalido:
    print(dni, end=" ")