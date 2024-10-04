from tkinter import * 


def anadir():
    listbox.insert(listbox.size(), entry_box.get())
    listbox.config(height=listbox.size())


window = Tk()

listbox = Listbox(window, selectmode=MULTIPLE)
listbox.pack()



listbox.insert(1, "Pizza")
listbox.insert(2, "Coca")

listbox.config(height=listbox.size())

entry_box = Entry(window)
entry_box.pack()

add_button = Button(window, text="Añadir", command=anadir)
add_button.pack()




window.mainloop()