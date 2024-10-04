import tkinter as tk

def saludar():
    print("Hola")

ventana = tk.Tk()

ventana.title("Mi primer ventana")
ventana.geometry("500x500")

etiqueta = tk.Label(ventana, text="Hola Mundo", font=("Arial",12))
etiqueta.pack()

boton = tk.Button(ventana, text="Saludar", font=("Arial",12), command=saludar)
boton.pack()

ventana.mainloop()