Algoritmo Ejercicio_6_Bisiesto
	escribir "introduzca el a?o para validar si es bisiesto"
	Leer año
	si (año mod 4 == 0) y (año mod 100 <> 0) o (año mod 400 = 0) Entonces
		Escribir "Bisiesto"
	SiNo
		Escribir"No es bisiesto"
	FinSi
	
FinAlgoritmo