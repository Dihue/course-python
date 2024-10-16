def contar_vacunas_genero(datos):
    """
    Cuenta cuántas personas han sido vacunadas según su género.

    Args:
        datos (list): Lista de diccionarios donde cada diccionario representa un registro de vacunación.

    Returns:
        tuple: Dos enteros, el primero es la cantidad de hombres vacunados ('M') y el segundo es la cantidad de mujeres vacunadas ('F').
    """
    # Contadores
    contador_masculino = 0
    contador_femenino = 0

    # Recorrer todos los registros
    for registro in datos:
        # Verificar y acumular en los contadores según el valor de "sexo"
        if registro["sexo"] == "M":
            contador_masculino += 1
        elif registro["sexo"] == "F":
            contador_femenino += 1
    
    return contador_masculino, contador_femenino


def tipo_vacuna_aplicada(datos):
    """
    Cuenta cuántas veces se ha aplicado cada tipo de vacuna.

    Args:
        datos (list): Lista de diccionarios donde cada diccionario representa un registro de vacunación.

    Returns:
        dict: Un diccionario donde las claves son los nombres de las vacunas y los valores son la cantidad de veces que han sido aplicadas.
    """
    vacunas = {}

    # Recorrer todos los registros
    for registro in datos:
        vacuna = registro["vacuna"]

        # Sumar al contador de la vacuna correspondiente
        if vacuna in vacunas:
            vacunas[vacuna] += 1
        else:
            vacunas[vacuna] = 1
    
    return vacunas


def dosis_por_jurisdiccion_residencia(datos):
    """
    Cuenta cuántas dosis fueron aplicadas en cada jurisdicción de residencia.

    Args:
        datos (list): Lista de diccionarios donde cada diccionario representa un registro de vacunación.

    Returns:
        dict: Un diccionario donde las claves son las jurisdicciones de residencia y los valores son la cantidad de dosis aplicadas.
    """
    jurisdicciones = {}

    # Recorrer todos los registros
    for registro in datos:
        jurisdiccion = registro["jurisdiccion_residencia"]

        # Sumar al contador de la jurisdicción correspondiente
        if jurisdiccion in jurisdicciones:
            jurisdicciones[jurisdiccion] += 1
        else:
            jurisdicciones[jurisdiccion] = 1
    
    return jurisdicciones


def segunda_dosis_jurisdiccion(datos):
    """
    Cuenta cuántas personas han recibido la segunda dosis en cada jurisdicción de residencia.

    Args:
        datos (list): Lista de diccionarios donde cada diccionario representa un registro de vacunación.

    Returns:
        dict: Un diccionario donde las claves son las jurisdicciones de residencia y los valores son la cantidad de personas que recibieron la segunda dosis.
    """
    segunda_dosis = {}

    # Recorrer todos los registros
    for registro in datos:
        if registro["nombre_dosis_generica"] == "2da":
            jurisdiccion = registro["jurisdiccion_residencia"]

            # Sumar al contador de la jurisdicción correspondiente
            if jurisdiccion in segunda_dosis:
                segunda_dosis[jurisdiccion] += 1
            else:
                segunda_dosis[jurisdiccion] = 1
    
    return segunda_dosis


def persona_mayor_60_refuerzo(datos):
    """
    Cuenta cuántas personas mayores de 60 años recibieron la dosis de refuerzo.

    Args:
        datos (list): Lista de diccionarios donde cada diccionario representa un registro de vacunación.

    Returns:
        int: La cantidad de personas mayores de 60 años que recibieron la dosis de refuerzo.
    """
    mayores_60_refuerzo = 0
    
    # Claves y valores esperados en los registros
    clave_1 = "grupo_etario"
    valor_1 = "60 o más años"

    clave_2 = "nombre_dosis_generica"
    valor_2 = "Refuerzo"

    # Recorrer todos los registros
    for registro in datos:
        # Verificar si el registro corresponde a una persona mayor de 60 años con refuerzo
        if registro[clave_1] == valor_1 and registro[clave_2] == valor_2:
            mayores_60_refuerzo += 1
    
    return mayores_60_refuerzo
