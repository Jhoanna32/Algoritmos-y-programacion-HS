Algoritmo Ejercicio_6_Bisiesto
	escribir "introduzca el a?o para validar si es bisiesto"
	Leer a�o
	si (a�o mod 4 == 0) y (a�o mod 100 <> 0) o (a�o mod 400 = 0) Entonces
		Escribir "Bisiesto"
	SiNo
		Escribir"No es bisiesto"
	FinSi
	
FinAlgoritmo