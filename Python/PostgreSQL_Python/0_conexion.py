import psycopg2

# Conectarnos a la base de datos (ya debe estar creada)
# Datos para la conexión en:
# PostgresSQL > Click derecho > Properties > Connection
conn = psycopg2.connect(database = "nombredb",
                        user = "postgres",
                        host = "localhost",
                        password = "didahue21",
                        port = 5432)

print("\n| - - - Conexión exitosa - - - |\n")