# ARCHIVOS
#? r -> solo lectura, w -> escritura, a -> append

#* Solo se ejecuta si el archivo existe
# archivo_personas = open("ejemplo.csv", "r")

#* Si el archivo no existe, lo crea mediando "w"
# archivo_personas = open("no_existe.csv", "w")

#* Escribe y pisa lo que ya estaba en el archivo
# archivo_personas.write("Hola,")
# archivo_personas.write("de nuevo,")
# archivo_personas.write("otra vez,")

#* Se abre en modo append y se agregará lo nuevo al final
# archivo_personas = open("no_existe.csv", "a")

#* Escribe a partir de lo que ya estaba en el archivo
# archivo_personas.write("\nAppend,")
# archivo_personas.write("en acción,")
# archivo_personas.write("otra vez,")

#* Cierra el archivo
# archivo_personas.close()

#* Abrir y mostrar linea a linea el contenido del archivo
with open("no_existe.csv", "r") as archivo:
    for linea in archivo:
        # evito el salto de linea extra del archivo
        # print(linea, end=" ")
        # otra forma de evitar el doble salto de linea
        print(linea.replace("\n", ""))