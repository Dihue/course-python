'''
Ejercicio 6: Centrar una cadena en la terminal

Escriba una función que tome una cadena de caracteres como primer
parámetro y el ancho de la terminal en caracteres como segundo
parámetro. Su función debe devolver una nueva cadena que consta
de la cadena original y el número correcto de espacios iniciales
para que la cadena original aparezca centrada dentro del ancho
proporcionado cuando se imprima. No agregue ningún carácter al
final de la cadena. Incluya un programa principal que use su función.
'''

def cadena_centrada(cadena,ancho):
	
	espacios = (ancho - len(cadena))//2

	separacion = " " * espacios

	print(f"{separacion}{cadena}{separacion}")


cadena = str(input("\nIngrese una cadena de caracteres: "))
ancho = int(input("\nIngrese el ancho de la terminal: "))

# 10
cadena_centrada(cadena,ancho)

'''
def palabla_centrada (cadena,ancho):
	print (cadena.center(ancho, " ")) 


palabla_centrada(cadena,ancho)
'''