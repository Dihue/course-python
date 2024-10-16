# Importa funciones relacionadas con el manejo de archivos CSV
from manejo_de_archivo import leer_archivo_csv, validar_datos
# Importa las funciones de procesamiento de datos
from funciones import (
    contar_vacunas_genero, 
    tipo_vacuna_aplicada, 
    dosis_por_jurisdiccion_residencia, 
    segunda_dosis_jurisdiccion, 
    persona_mayor_60_refuerzo
)


# Nombre del archivo CSV que contiene los datos de vacunación
NOMBRE_DEL_ARCHIVO = "datos_nomivac_parte1.csv"

# Leer los datos del archivo CSV
datos_generales = leer_archivo_csv(NOMBRE_DEL_ARCHIVO)

# Validar los datos y separar registros válidos de inconsistencias
datos_validos = validar_datos(datos_generales)


# Contar la cantidad de personas vacunadas por género
contador_masculino, contador_femenino = contar_vacunas_genero(datos_validos)

# Mostrar en pantalla el total de personas vacunadas por género
print("\nPersonas vacunadas por género")
print(f"|-> Masculino: {contador_masculino}")
print(f"|-> Femenino: {contador_femenino}")


# Contar el tipo de vacunas aplicadas
vacunas = tipo_vacuna_aplicada(datos_validos)

# Mostrar en pantalla la proporción de vacunas aplicadas por tipo
print("\nVacunas aplicadas por tipo")
for vacuna, cantidad in vacunas.items():
    total_vacunas = len(datos_validos)
    proporcion = (cantidad / total_vacunas) * 100
    print(f"|-> {vacuna}: {proporcion:.2f}%")  # Mostrar el porcentaje de cada tipo de vacuna


# Contar la cantidad de dosis aplicadas por jurisdicción de residencia
jurisdicciones = dosis_por_jurisdiccion_residencia(datos_validos)

# Mostrar en pantalla la cantidad de dosis aplicadas en cada jurisdicción de residencia
print("\nDosis por jurisdiccion de residencia")
for jurisdiccion, cantidad in jurisdicciones.items():
    print(f"|-> {jurisdiccion}: {cantidad} dosis")


# Contar la cantidad de personas que recibieron la segunda dosis por jurisdicción
segunda_dosis = segunda_dosis_jurisdiccion(datos_validos)

# Mostrar en pantalla la cantidad de personas que recibieron la segunda dosis en cada jurisdicción
print("\nPersonas que recibieron la segunda dosis por jurisdicción")
for jurisdiccion, cantidad in segunda_dosis.items():
    print(f"|-> {jurisdiccion}: {cantidad} personas")


# Contar cuántas personas mayores de 60 años recibieron la dosis de refuerzo
mayores_60_refuerzo = persona_mayor_60_refuerzo(datos_validos)
mensaje = "Personas mayores de 60 años que recibieron la dosis de refuerzo"
print(f"\n{mensaje}: {mayores_60_refuerzo}")
