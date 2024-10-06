# 1° Imports
import validador
# 2° Librerias de Terceros
# 3° Librerias Propias
# from validador import todo_es_un_numero, rango_valido


def validar_documentos(lista_documentos):
    lista_documentos_validos = []
    lista_documentos_invalidos = []

    for doc in lista_documentos:
        doc = doc.replace(".", "")

        if not validador.todo_es_un_numero(doc):
            lista_documentos_invalidos.append({
                "Value": doc,
                "Error": "Tiene caracteres especiales"
            })
            continue

        doc = int(doc)

        if not validador.rango_valido(doc):
            lista_documentos_invalidos.append({
                "Value": doc,
                "Error": "Longitud incorrecta"
            })
            continue

        lista_documentos_validos.append(doc)
    
    return lista_documentos_validos, lista_documentos_invalidos