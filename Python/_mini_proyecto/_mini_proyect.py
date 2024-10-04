import tkinter as tk
from tkinter import ttk
import pytz
from datetime import datetime

# Diccionario de zonas horarias por país
zonas_horarias = {
    "Argentina": "America/Argentina/Buenos_Aires",
    "España": "Europe/Madrid",
    "Australia": "Australia/Sydney"
}

# Función para actualizar el reloj según la zona horaria seleccionada
def actualizar_reloj():
    zona_seleccionada = variable_opcion.get()  # Obtener la opción seleccionada
    zona_horaria = pytz.timezone(zonas_horarias[zona_seleccionada])  # Obtener la zona horaria
    tiempo_actual = datetime.now(zona_horaria).strftime('%H:%M:%S')  # Obtener la hora actual en la zona horaria
    label_reloj.config(text=f"Hora actual en {zona_seleccionada}: {tiempo_actual}")  # Mostrar el país y la hora
    label_reloj.after(1000, actualizar_reloj)  # Actualizar cada segundo

# Función para cambiar la zona horaria según el país seleccionado
def cambiar_zona_horaria(pais):
    variable_opcion.set(pais)  # Cambiar el valor seleccionado
    actualizar_reloj()         # Actualizar el reloj inmediatamente

# Función para agregar una tarea a la lista
def agregar_tarea():
    pais = entrada_pais.get()
    ciudad = entrada_ciudad.get()
    if pais != "" and ciudad != "":
        tarea = f"{pais}: {ciudad}"  # Formato "País: Ciudad"
        lista_tareas.insert(tk.END, tarea)
        entrada_pais.delete(0, tk.END)
        entrada_ciudad.delete(0, tk.END)

# Función para eliminar la tarea seleccionada
def eliminar_tarea():
    seleccion = lista_tareas.curselection()  # Obtener el índice de la tarea seleccionada
    if seleccion:  # Verificar que haya una selección
        lista_tareas.delete(seleccion[0])  # Eliminar la tarea seleccionada

# Función para seleccionar una tarea de la lista y rellenar los campos
def seleccionar_tarea():
    seleccion = lista_tareas.curselection()  # Obtener el índice de la tarea seleccionada
    if seleccion:  # Verificar que haya una selección
        tarea_seleccionada = lista_tareas.get(seleccion[0])  # Obtener el texto de la tarea
        pais, ciudad = tarea_seleccionada.split(": ")  # Separar País y Ciudad
        entrada_pais.delete(0, tk.END)
        entrada_pais.insert(tk.END, pais)
        entrada_ciudad.delete(0, tk.END)
        entrada_ciudad.insert(tk.END, ciudad)

# Función para modificar la tarea seleccionada
def modificar_tarea():
    seleccion = lista_tareas.curselection()  # Obtener el índice de la tarea seleccionada
    if seleccion:  # Verificar que haya una selección
        pais = entrada_pais.get()
        ciudad = entrada_ciudad.get()
        if pais != "" and ciudad != "":
            tarea_modificada = f"{pais}: {ciudad}"  # Formato "País: Ciudad"
            lista_tareas.delete(seleccion[0])  # Eliminar la tarea actual
            lista_tareas.insert(seleccion[0], tarea_modificada)  # Insertar la tarea modificada en el mismo lugar
            entrada_pais.delete(0, tk.END)
            entrada_ciudad.delete(0, tk.END)
        else:
            tk.messagebox.showwarning("Advertencia", "Por favor, complete ambos campos.")

# Crear la ventana principal
root = tk.Tk()
root.title("Aplicación Tkinter")
root.geometry("400x400")

# Variable para almacenar la opción seleccionada del menú
variable_opcion = tk.StringVar(root)
variable_opcion.set("Argentina")  # Valor por defecto

# Crear la barra de menú en la parte superior
barra_menu = tk.Menu(root)
root.config(menu=barra_menu)

# Crear el menú de "Horarios"
menu_horarios = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Horarios", menu=menu_horarios)

# Agregar las opciones de los países al menú "Horarios"
menu_horarios.add_command(label="Argentina", command=lambda: cambiar_zona_horaria("Argentina"))
menu_horarios.add_command(label="España", command=lambda: cambiar_zona_horaria("España"))
menu_horarios.add_command(label="Australia", command=lambda: cambiar_zona_horaria("Australia"))

# Reloj en la parte superior
label_reloj = tk.Label(root, font=('calibri', 20, 'bold'), foreground='black')
label_reloj.pack(pady=10)
actualizar_reloj()

# Frame para contener la lista de tareas y el scrollbar
frame_tareas = tk.Frame(root)
frame_tareas.pack(pady=10)

# Scrollbar para la lista de tareas
scrollbar = tk.Scrollbar(frame_tareas)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Lista de tareas (Listbox)
lista_tareas = tk.Listbox(frame_tareas, yscrollcommand=scrollbar.set, height=10, width=40)
lista_tareas.pack(side=tk.LEFT)
scrollbar.config(command=lista_tareas.yview)

# Frame para las entradas de País y Ciudad
frame_entradas = tk.Frame(root)
frame_entradas.pack(pady=10)

# Entrada de País con su etiqueta
label_pais = tk.Label(frame_entradas, text="País")
label_pais.pack(side=tk.LEFT, padx=5)
entrada_pais = tk.Entry(frame_entradas, width=15)
entrada_pais.pack(side=tk.LEFT, padx=5)

# Entrada de Ciudad con su etiqueta
label_ciudad = tk.Label(frame_entradas, text="Ciudad")
label_ciudad.pack(side=tk.LEFT, padx=5)
entrada_ciudad = tk.Entry(frame_entradas, width=15)
entrada_ciudad.pack(side=tk.LEFT, padx=5)

# Frame para contener los botones lado a lado
frame_botones = tk.Frame(root)
frame_botones.pack(pady=10)

# Botón para agregar tareas
boton_agregar = tk.Button(frame_botones, text="Agregar", command=agregar_tarea)
boton_agregar.pack(side=tk.LEFT, padx=5)

# Botón para eliminar la tarea seleccionada
boton_eliminar = tk.Button(frame_botones, text="Eliminar", command=eliminar_tarea)
boton_eliminar.pack(side=tk.LEFT, padx=5)

# Botón para seleccionar la tarea a modificar
boton_seleccionar = tk.Button(frame_botones, text="Seleccionar", command=seleccionar_tarea)
boton_seleccionar.pack(side=tk.LEFT, padx=5)

# Botón para modificar la tarea seleccionada
boton_modificar = tk.Button(frame_botones, text="Modificar", command=modificar_tarea)
boton_modificar.pack(side=tk.LEFT, padx=5)

# Iniciar el loop de la aplicación
root.mainloop()
