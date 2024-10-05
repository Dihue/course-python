LISTA_DOCUMENTOS = [
    "123",
    "43547567",
    "21.434.877",
    "1231231231231",
    "0",
    "000000",
    "...345"
]

lista_documentos_validos = []
lista_documentos_invalidos = []


for doc in LISTA_DOCUMENTOS:
    # Reemplaza "." por ""
    doc = doc.replace(".", "")

    # Si documento no es numérico
    if not doc.isnumeric():
        # lista_documentos_invalidos.append(doc)
        lista_documentos_invalidos.append({
            "value": doc,
            "error": "tiene caracteres especiales"
        })
        continue

    doc = int(doc)

    # Validación entre valores limite
    if not (999999 < doc <100000000):
        # lista_documentos_invalidos.append(doc)
        lista_documentos_invalidos.append({
            "value": doc,
            "error": "longitud incorrecta"
        })
        continue

    lista_documentos_validos.append(doc)

print("\nDocumentos válidos: ", lista_documentos_validos)
print("\nDocumentos inválidos: ", lista_documentos_invalidos)