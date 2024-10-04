import sqlite3

# Define la ruta del archivo de la base de datos
ruta_base_datos = "D:/Users/Dihue/Desktop/Python/SQLite_Python/data.db"

# Conectarnos a la base de datos
conn = sqlite3.connect(ruta_base_datos)

# Mensaje de control de la conezión
print("\nConexión exitosa de la base de datos")

# Sentencia de consulta de dato
cursor = conn.execute("SELECT id, nombre, direccion from PERSONA")

# Mostrar los datos obtenidos de la DB
for row in cursor:
    print("ID = ", row[0])
    print("NOMBRE = ", row[1])
    print("DIRECCION = ", row[2], "\n")

print("Operación exitosa")

# Cierre de la conexión
conn.close()