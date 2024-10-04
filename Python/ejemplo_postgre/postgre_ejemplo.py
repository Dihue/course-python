import psycopg2 # type: ignore

conn = psycopg2.connect(database = "database",
                        user = "postgres",
                        host = "localhost",
                        password = "didahue21",
                        port = "5432")

cur = conn.cursor()

cur.execute('''
            ''')

conn.commit()

cur.close()
conn.close()