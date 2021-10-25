contador1 = 0

while contador1 < 10:
	contador2 = 0

	while contador2 < 10:
		if contador2 == 5:
			break

		contador2 += 1
	contador1 += 1

print(contador1)