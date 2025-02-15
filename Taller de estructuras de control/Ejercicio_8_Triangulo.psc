Algoritmo Ejercicio_8_Triangulo
	// Entradas
    Definir Lado1, Lado2, Lado3, area Como Real
	Escribir "Ingrese la longitud del lado1: "
    Leer Lado1
    Escribir "Ingrese la longitud del lado2: "
    Leer Lado2
    Escribir "Ingrese la longitud del lado3: "
    Leer Lado3
	
	//Caja negra
	semi<-(lado_uno+lado_dos+lado_tres)/2
	area<-((semi*(semi-lado1)*(semi-lado2)*(semi-lado3)))^(1/2)
	
	//Salida
	Escribir "El área del triángulo es: ", area
FinAlgoritmo
