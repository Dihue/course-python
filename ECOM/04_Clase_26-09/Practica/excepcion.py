persona = {
    "nombre": "Dihue",
    "apellido": "De Cuadra",
    "direccion": "Calle 123"
}

# Es una estructura de control
# try / except
direccion = None
try:
    direccion = persona["direccion"]
    x = 10 / 2
# captura de la excepcion
# except Exception as e:
except ZeroDivisionError:
    print("No se puede dividir por cero")

except Exception as la_excepcion:
    print("ha ocurrido un error", la_excepcion.__class__.__name__)

else:
    print("ELSE --> Ninguna excepción ocurrio")

finally:
    print("FINALLY --> Siempre se ejecuta")

# validar si es de un tipo de dato (None)
if direccion is not None:
    print(f"La dirección de la persona es {direccion}")