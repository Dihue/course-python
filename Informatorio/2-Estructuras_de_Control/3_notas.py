preguntas = int(input("\nCantidad de preguntas del examen:"))
correctas = int(input("\nCantidad de respuestas correctas:"))

porcentaje = (correctas * 100) / preguntas

if (90 <= porcentaje <= 100):
	print("Nota del alumno: EXCELENTE")
elif (80 <= porcentaje < 90):
	print("Nota del alumno: DISTINGUIDO")
elif (70 <= porcentaje < 80):
	print("Nota del alumno: MUY BUENO")
elif (60 <= porcentaje < 70):
	print("Nota del alumno: APROBADO")
elif (0 <= porcentaje < 60):
	print("Nota del alumno: INSUFICIENTE")
else:
	print("Examen denegado")