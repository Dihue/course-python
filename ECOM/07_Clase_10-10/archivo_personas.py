encabezado = None # evitar posible error

# Codifico al archivo mediante encoding (toma las tildes)
with open("personas.csv", "r", encoding="utf-8") as archivo:
    # Enumerate enumera cada linea del archivo
    # Desempaqueto la posición y la linea del archivo
    for pos, linea in enumerate(archivo):
        # print("pos:", pos) # solo control
        persona_raw = linea.replace("\n", "")

        # Condición para tomar solo la primer linea
        if pos == 0:
            # Divido solo la primer linea según el caracter especial
            # Se almacena en la lista "encabezado"
            encabezado = persona_raw.split(";")
            # print("Encabezado:", encabezado) # solo control
            continue

        # Divide cada fila del registro según el caracter especial
        # por lo que queda cada persona con sus datos por cada linea
        # para luego ser almacenada en la lista "persona"
        persona = persona_raw.split(";")
        # print("pos:", pos) # solo control
        # print("Persona", persona.__class__.__name__)
        # print("Lista personas:", persona)

        # Diccionario vacío
        persona_dict = {}

        # Se enumera lo que se volverá las key del diccionario y se
        # las desempaqueta en el "index" que será la posición y en
        # "titulo" que será el nombre/valor de la key
        for index, titulo in enumerate(encabezado):
            # Asigno al diccionario el nombre de la key con "titulo"
            # y a la persona con su respectivo "index" por ser la forma
            # de acceso que tiene una lista
            persona_dict[titulo] = persona[index]


        print(persona_dict)