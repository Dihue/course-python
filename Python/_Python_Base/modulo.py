import datetime

def cantidad_dias():
    dia = int(input("Ingrese día: "))
    mes = int(input("Ingrese mes: "))
    anio = int(input("Ingrese año: "))

    fecha_inicio = datetime.date(2024,9,1)
    fecha_intro = datetime.date(anio,mes,dia)

    cantidad = fecha_intro - fecha_inicio
    print(f"\nLa cantidad de días es {cantidad}")

cantidad_dias()