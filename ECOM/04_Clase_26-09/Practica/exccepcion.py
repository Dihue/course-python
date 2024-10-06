persona = {
    "nombre": "Dihue",
    "apellido": "De Cuadra"
}

# Es una estructura de control
# try / except
direccion = None
try:
    direccion = persona["direccion"]
# captura de la excepcion
# except Exception as e:
except Exception as la_excepcion:
    print("ha ocurrido un error", la_excepcion.__class__.__name__)

# validar si es de un tipo de dato (None)
if direccion is not None:
    print(f"La dirección de la persona es {direccion}")