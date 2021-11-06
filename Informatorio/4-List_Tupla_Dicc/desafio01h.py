'''
Construya un algoritmo que sume todos los elementos en posición par de una lista.
'''

lista0 = [23,'asd','zxc',91,73,'qwe','jkl']

lista1 = ['asd','zxc','qwe','jkl','iop','bnm']

lista = [12,23,34,45,56,67,78,89,90]

#print(lista[0])
#print(len(lista))
'''
def indice(listado):
	contador = 0
	while contador <= len(listado):
		if (contador % 2) == 0:
			print(f"Indice {contador}, elemento: {listado[contador]}")
		contador += 1

indice(lista)
'''
suma = 0
for x in range (0, len(lista), 2 ):
	print(lista[x])
	suma = suma + lista[x]

print(suma)