import psycopg2

conn = psycopg2.connect(database = "nombredb",
                        user = "postgres",
                        host = "localhost",
                        password = "didahue21",
                        port = 5432)

print("\n| - - - Conexión exitosa - - - |\n")

cur = conn.cursor()

cur.execute("""SELECT * FROM PERSONA ORDER BY NOMBRE""")

rows = cur.fetchall()

# Para guardar los cambios
conn.commit()

cur.close
# Cerrar la conexión
conn.close()
print("\n| - - - Conexión cerrada - - - |\n")

for row in rows:
    print(row)