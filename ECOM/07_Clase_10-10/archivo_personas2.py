encabezado = None # evitar posible error
todas_las_personas = []

def todo_es_un_numero(valor):
    return valor.isnumeric()

# Codifico al archivo mediante encoding (toma las tildes)
with open("personas.csv", "r", encoding="utf-8") as archivo:
    # Enumerate enumera cada linea del archivo
    # Desempaqueto la posición y la linea del archivo
    for pos, linea in enumerate(archivo):
        persona_raw = linea.replace("\n", "")

        # Condición para tomar solo la primer linea
        if pos == 0:
            # Divido solo la primer linea según el caracter especial
            # Se almacena en la lista "encabezado"
            encabezado = persona_raw.split(";")
            continue

        # Divide cada fila del registro según el caracter especial
        # por lo que queda cada persona con sus datos por cada linea
        # para luego ser almacenada en la lista "persona"
        persona = persona_raw.split(";")

        # Diccionario por comprensión
        # "titulo" como clase y "persona[index]" como valor
        # por lo que se general el diccionario de forma dinámica
        persona_dict = {titulo: persona[index] for index, titulo in enumerate(encabezado)}

        if todo_es_un_numero(persona_dict["dni"]):
            todas_las_personas.append(persona_dict)

print("Lista de personas:", todas_las_personas)