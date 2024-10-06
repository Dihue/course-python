# # Abriendo y leyendo el archivo completo
# with open('http_access_200304.log', 'r') as archivito:
#     contenido = archivito.read()  # Lee todo el contenido del archivo
#     print(contenido[:500])      # Imprime los primeros 500 caracteres

# leer linea por linea
# with open('http_access_200304.log', 'r') as archivo:
#     for linea in archivo:
#         print(linea.strip())  # Imprime cada línea sin los saltos de línea adicionales

# guardar las lineas en una lista:
# with open('http_access_200304.log', 'r') as archivo:
#     lineas = archivo.readlines()  # Lee todas las líneas y las guarda en una lista
#     print(lineas[:5])             # Imprime las primeras 5 líneas

# escribir en un nuevo archivo el proceso
# with open('http_access_200304.log', 'r') as archivo:
#     with open('resumen_codigos_http.txt', 'w') as archivo_salida:
#         for linea in archivo:
#             partes = linea.split(" ")
#             codigo_respuesta = partes[-2]
#             archivo_salida.write(f"Código HTTP: {codigo_respuesta}\n")
