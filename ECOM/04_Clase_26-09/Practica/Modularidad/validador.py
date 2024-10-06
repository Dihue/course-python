def todo_es_un_numero(valor):
    return valor.isnumeric()

def rango_valido(valor):
    return (999999 < valor <100000000)

# Hace que las pruebas, solo se inicien, cuando este archivo
# sea considerado como main al momento de la ejecución del
# programa
if __name__ == "__main__":
    # Pruebas
    print("\nMódulo del validador")
    print(todo_es_un_numero("asd"))
    print(todo_es_un_numero("123123"))
    print("VALIDADOR -->", __name__)
    print("==========================")