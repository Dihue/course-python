import psycopg2

conn = psycopg2.connect(database = "nombredb",
                        user = "postgres",
                        host = "localhost",
                        password = "didahue21",
                        port = 5432)

print("\n| - - - Conexión exitosa - - - |\n")

cur = conn.cursor()

cur.execute("""INSERT INTO PERSONA(ID, NOMBRE, EDAD, DIRECCION)
            VALUES(1,'Maria',23,'Calle Falsa 123');""")

cur.execute("""INSERT INTO PERSONA(ID, NOMBRE, EDAD, DIRECCION)
            VALUES(2,'Juan',12,'Avenida Falsa 321');""")

cur.execute("""INSERT INTO PERSONA(ID, NOMBRE, EDAD, DIRECCION)
            VALUES(3,'Pedro',34,'Por ahi 123');""")

print("\n| - - - Datos ingresados exitosamente - - - |\n")

# Para guardar los cambios
conn.commit()

cur.close
# Cerrar la conexión
conn.close()
print("\n| - - - Conexión cerrada - - - |\n")