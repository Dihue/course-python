import psycopg2

conn = psycopg2.connect(database = "nombredb",
                        user = "postgres",
                        host = "localhost",
                        password = "didahue21",
                        port = 5432)

print("\n| - - - Conexión exitosa - - - |\n")

cur = conn.cursor()

cur.execute("""DELETE FROM PERSONA WHERE NOMBRE = 'Pedro'""")

print("\n| - - - Datos actualizados exitosamente - - - |\n")

# Para guardar los cambios
conn.commit()

cur.close
# Cerrar la conexión
conn.close()
print("\n| - - - Conexión cerrada - - - |\n")