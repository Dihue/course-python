persona = {
    "nombre", "Dihue",
    "apellido", "De Cuadra"
}

# try / except
direccion = None
try:
    direccion = persona["direccion"]

except:
    print("ha ocurrido un error")

if direccion is not None:
    print(f"La dirección de la persona es {direccion}")