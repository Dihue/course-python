'''
Cargue dos listas, y actualice la primer lista con los elementos que están en la segunda y no en la primera
'''

#lista1 = [12,23,34]

lista2 = ['qwe','asd','zxc']
'''
cont = 0

for x in lista2:
	if cont <= len(lista2):
		lista1[cont] = lista2[x]
		cont += 1

print(lista1)
'''

originar = list(lista2)

lista2.reverse()

print(originar)
print(lista2)