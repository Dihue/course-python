# 1° Imports
# 2° Librerias de Terceros
# 3° Librerias Propias
from parametros import LISTA_DOCUMENTOS
from core import validar_documentos

# Desempaquetado de valores de forma manual
valores = validar_documentos(LISTA_DOCUMENTOS)
print("Valores --> ", valores.__class__.__name__)
# print("Valores --> ", valores)

# lista_doc_validos = valores[0]
# lista_doc_invalidos = valores[1]

# Desempaquetado de valores automatico
lista_doc_validos, lista_doc_invalidos = validar_documentos(LISTA_DOCUMENTOS)
# print("MAIN -->", __name__)
print("\nDocumentos válidos: ", lista_doc_validos)
print("\nDocumentos inválidos: ", lista_doc_invalidos)