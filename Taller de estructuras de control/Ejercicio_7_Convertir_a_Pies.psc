Algoritmo Ejercicio_7_Convertir_a_Pies
	// Entradas
    Definir metros, pulgadas_totales, pies, pulgadas_restantes Como Real
    Escribir "Ingrese la cantidad en metros: "
    Leer metros
	
    // Caja negra
    pulgadas_totales = metros * 39.27
    pies = Trunc(pulgadas_totales / 12)
    pulgadas_restantes = pulgadas_totales % 12
	
    // Salidas
    Escribir "La cantidad en pies es: ", pies
    Escribir "La cantidad restante en pulgadas es: ", pulgadas_restantes
FinAlgoritmo
