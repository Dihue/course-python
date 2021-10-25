'''
Escribir un programa que pregunte a diferentes personas cuánto
conocen sobre contaminación del 1 al 10, almacene estos valores
en una lista y los muestre por pantalla ordenados de menor a
mayor.
'''
lista = list()

pregunta = input("\n¿Desea contestar una pregunta sobre contaminación?\n1-SI\n2-NO\n")

while pregunta == '1':
	opinion = input("\n¿Cuánto conoce de contaminación? Del 1 al 10: ")
	lista.append(opinion)

	pregunta = input("\n¿Desea contestar una pregunta sobre contaminación?\n1-SI\n2-NO\n")

lista.sort()

print(lista)