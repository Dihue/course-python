import sqlite3

# Define la ruta del archivo de la base de datos
ruta_base_datos = "D:/Users/Dihue/Desktop/Python/SQLite_Python/data.db"

# Conectarnos a la base de datos
conn = sqlite3.connect(ruta_base_datos)

# Mensaje de control de la conezión
print("Conexión exitosa de la base de datos")

# Creación de una tabla
conn.execute('''CREATE TABLE PERSONA (
             ID INT PRIMARY KEY NOT NULL,
             NOMBRE TEXT NOT NULL,
             EDAD INT NOT NULL,
             DIRECCION CHAR(50));''')

# Mensaje de contro de creación de la tabla
print("Tabla creada exitosamente")

# Cierre de la conexión
conn.close