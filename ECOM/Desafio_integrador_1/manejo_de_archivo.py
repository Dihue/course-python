def leer_archivo_csv(nombre_archivo, delimitador=','):
    """
    Lee un archivo CSV y lo almacena en una lista de diccionarios.

    Args:
        nombre_archivo (str): Nombre del archivo CSV a leer.
        delimitador (str): Delimitador usado en el archivo CSV (por defecto ',').

    Returns:
        list: Lista de diccionarios, donde cada diccionario representa una fila del archivo CSV.

    Raises:
        FileNotFoundError: Si el archivo no se encuentra.
        ValueError: Si el formato del archivo no es consistente.
    """
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
    except FileNotFoundError:
        print(f"Error: El archivo {nombre_archivo} no fue encontrado.")
        return []

    # Obtener los encabezados
    encabezados = lineas[0].strip().split(delimitador)

    # Lista para almacenar datos
    datos = []

    # Recorrer línea a línea a partir de la línea 1
    for linea in lineas[1:]:
        valores = linea.strip().split(delimitador)

        # Validar si la cantidad de columnas coincide con los encabezados
        if len(valores) != len(encabezados):
            print(f"Error: Inconsistencia en la cantidad de columnas en la línea: {linea}")
            continue

        # Crear un diccionario para la fila actual
        registro = dict(zip(encabezados, valores))

        # Agregar el diccionario a la lista de datos
        datos.append(registro)

    return datos


def procesar_inconsistencias(inconsistencias):
    """
    Procesa los registros que tienen inconsistencias y los guarda en un archivo CSV.

    Args:
        inconsistencias (list): Lista de diccionarios que representan los registros con inconsistencias.
    
    Retorna:
        None. Los datos son guardados en el archivo 'inconsistencias.csv'.
    """
    if inconsistencias:
        # Abre o crea el archivo 'inconsistencias.csv' en modo escritura
        with open("inconsistencias.csv", "w", encoding="utf-8") as archivo:
            # Escribe los encabezados del archivo usando las claves del primer registro
            encabezado = ",".join(inconsistencias[0].keys())
            archivo.write(encabezado + "\n")

            # Escribe cada registro en el archivo
            for registro in inconsistencias:
                fila = ",".join(registro.values())
                archivo.write(fila + "\n")
    else:
        print("No se encontraron inconsistencias")


def procesar_datos_validos(datos_validos):
    """
    Procesa los registros válidos y los guarda en un archivo CSV.

    Args:
        datos_validos (list): Lista de diccionarios que representan los registros válidos.
    
    Retorna:
        None. Los datos son guardados en el archivo 'datos_validos.csv'.
    """
    if datos_validos:
        # Abre o crea el archivo 'datos_validos.csv' en modo escritura
        with open("datos_validos.csv", "w", encoding="utf-8") as archivo:
            # Escribe los encabezados del archivo usando las claves del primer registro
            encabezado = ",".join(datos_validos[0].keys())
            archivo.write(encabezado + "\n")

            # Escribe cada registro en el archivo
            for registro in datos_validos:
                fila = ",".join(registro.values())
                archivo.write(fila + "\n")
    else:
        print("No hay datos válidos para procesar")


def validar_datos(datos):
    """
    Valida una lista de registros, separando aquellos con inconsistencias de los válidos.

    Revisa cada campo de los registros en busca de valores vacíos o con "S.I." (sin información).
    Si un registro tiene inconsistencias, agrega una observación en el campo "Observación".
    Luego, los registros válidos y con inconsistencias son guardados en archivos CSV separados.

    Args:
        datos (list): Lista de diccionarios donde cada diccionario representa un registro de datos.

    Returns:
        list: Lista de registros válidos.
    """
    inconsistencias = []
    datos_validos = []

    for registro in datos:
        observacion = ""  # Inicializa la observación vacía para cada registro
        
        # Itera sobre los campos y valores de cada registro
        for clave, valor in registro.items():
            # Verifica si el valor está vacío o es "S.I."
            if valor == "" or valor == "S.I.":
                observacion += f"Falta valor en {clave}, "  # Añade a la observación
        
        # Si hay alguna observación, marca el registro como inconsistente
        if observacion:
            registro["Observación"] = observacion.strip(", ")  # Elimina la coma final
            inconsistencias.append(registro)
        else:
            datos_validos.append(registro)  # Si no hay observaciones, el registro es válido

    # Procesa y guarda los registros con inconsistencias y los válidos
    procesar_inconsistencias(inconsistencias)
    procesar_datos_validos(datos_validos)

    return datos_validos
