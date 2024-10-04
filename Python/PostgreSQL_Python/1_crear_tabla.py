import psycopg2

conn = psycopg2.connect(database = "nombredb",
                        user = "postgres",
                        host = "localhost",
                        password = "didahue21",
                        port = 5432)

print("\n| - - - Conexión exitosa - - - |\n")

cur = conn.cursor()

cur.execute("""CREATE TABLE PERSONA(
            ID INT PRIMARY KEY NOT NULL,
            NOMBRE TEXT NOT NULL,
            EDAD INT NOT NULL,
            DIRECCION CHAR(50));""")

print("\n| - - - Tabla creada exitosamente - - - |\n")

# Para guardar los cambios
conn.commit()

cur.close
# Cerrar la conexión
conn.close()
print("\n| - - - Conexión cerrada - - - |\n")