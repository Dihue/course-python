import sqlite3

# Define la ruta del archivo de la base de datos
ruta_base_datos = "D:/Users/Dihue/Desktop/Python/SQLite_Python/data.db"

# Conectarnos a la base de datos
conn = sqlite3.connect(ruta_base_datos)

# Mensaje de control de la conezión
print("\nConexión exitosa de la base de datos")

# Insertar datos en una tabla SQLite
conn.execute("INSERT INTO PERSONA (ID,NOMBRE,EDAD,DIRECCION)\
             VALUES (1,'Pablo',21,'Calle sin número')")

conn.execute("INSERT INTO PERSONA (ID,NOMBRE,EDAD,DIRECCION)\
             VALUES (2,'Maria',19,'Avenida Por Ahi')")

conn.commit()
print("Registros agregados exitosamente")

conn.close()