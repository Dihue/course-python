import sqlite3
from tkinter import *

# Configuración de la raíz
root = Tk()
root.title("Restaurante Plato's - Menú")
root.resizable(0,0) # Ventana no redimensionable
root.iconbitmap('menu_restaurante_sqlite3_tkinter\cuchillo_tenedor.ico')
root.config(bd=25, relief="sunken")


Label(root, text="  Restaurante Plato's   ", fg="brown4", font=("Times New Roman",28,"bold italic")).pack()
Label(root, text="Menú del día", fg="red", font=("Times New Roman",24,"bold italic")).pack()
imagen=PhotoImage(file="menu_restaurante_sqlite3_tkinter\logoplatos.png")
Label(root, image=imagen, width=200,height=200).pack()


# Separación entre títulos y categorias
Label(root, text=" ").pack()
#-----------------------------
ruta_base_datos = "D:/Users/Dihue/Desktop/Python/menu_restaurante_sqlite3_tkinter/menu_restaurante.db"

#Nos conectamos a la base de datos
conexion = sqlite3.connect(ruta_base_datos)
cursor = conexion.cursor()


# Buscamos las categorías y platos de la base de datos
# Código igual que mostrar_menu() de menu_restaurante.py, pero adaptado a interfaz gráfica
categorias = cursor.execute("SELECT * FROM categoria").fetchall()
for categoria in categorias:
	Label(root, text=categoria[1], fg="black", font=("Times New Roman",20,"bold italic")).pack()

	platos = cursor.execute("SELECT * FROM plato WHERE categoria_id={}".format(categoria[0])).fetchall()
	for plato in platos:
		Label(root, text=plato[1], fg="gray", font=("Verdana",15,"italic")).pack()

	# Separación entre categorias
	Label(root, text="*****").pack()

conexion.close()  # Cerramos la conexión con la base de datos

#-----------------------------
# Precio del menú
Label(root, text="Precio: $1000 (IVA incluido)", fg="brown4", font=("Times New Roman",15,"bold italic")).pack(side="right")

# Bucle aplicación
root.mainloop()