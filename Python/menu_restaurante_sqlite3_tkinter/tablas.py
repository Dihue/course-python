import sqlite3

ruta_base_datos = "D:/Users/Dihue/Desktop/Python/menu_restaurante_sqlite3_tkinter/menu_restaurante.db"

#Nos conectamos a la base de datos
conexion = sqlite3.connect(ruta_base_datos)
cursor = conexion.cursor()

cursor.execute('''CREATE TABLE categoria(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre VARCHAR(100) UNIQUE NOT NULL)''')

print("La tabla de Categorías se ha creado correctamente.")

cursor.execute('''CREATE TABLE plato(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre VARCHAR(100) UNIQUE NOT NULL,
                categoria_id INTEGER NOT NULL,
                FOREIGN KEY(categoria_id) REFERENCES categoria(id))''')

print("La tabla de Platos se ha creado correctamente.")

conexion.close()