from tkinter import *


# Crear la ventana principal
root = Tk()
root.title("Agenda de Contactos")
root.geometry("500x400")

# Frame para la entrada de DATOS
frame_entradas = Frame(root)
frame_entradas.pack(pady=10)

# Etiqueta DATOS
label_titulo = Label(frame_entradas, text="Datos del Contacto\n")
label_titulo.grid(row=0, column=1)

# Entrada de NOMBRE con su etiqueta
label_nombre = Label(frame_entradas, text="Nombre: ")
label_nombre.grid(row=1, column=0, sticky=W)
entrada_nombre = Entry(frame_entradas, width=25)
entrada_nombre.grid(row=1, column=1)

# Entrada de APELLIDO con su etiqueta
label_apellido = Label(frame_entradas, text="Apellido: ")
label_apellido.grid(row=2, column=0, sticky=W)
entrada_apellido = Entry(frame_entradas, width=25)
entrada_apellido.grid(row=2, column=1)

# Entrada de TELEFONO con su etiqueta
label_telefono = Label(frame_entradas, text="Teléfono: ")
label_telefono.grid(row=3, column=0, sticky=W)
entrada_telefono = Entry(frame_entradas, width=25)
entrada_telefono.grid(row=3, column=1)

# Inicia el loop de la aplicación
root.mainloop()
