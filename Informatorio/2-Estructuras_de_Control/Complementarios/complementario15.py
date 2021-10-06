'''
Un obrero necesita calcular su salario semanal, el cual se obtiene
de la siguiente manera:

1. Si trabaja 40 hs o menos, se le paga $16 por hora
2. SI trabaja mas de 40 hs, se le paga $16 por cada una de las primeras
40 hs y $20 por cada hora extra
'''

hs_trabajadas = int(input("\nIngresar horas trabajadas: "))

base = 40 * 16
extra = (hs_trabajadas - 40) * 20

if hs_trabajadas <= 40:
	total = hs_trabajadas * 16

elif hs_trabajadas > 40:
	total = base + extra

print(f"\nEl salario semanal es de {total}")


'''

horas = int(input("Ingresar las horas trabajas: "))

if horas <= 40:
	total = horas * 16
else:
	total = (horas-40) * 20 + (40*20)

'''