Algoritmo Ejercicio_14_luz
	// Entradas
    Definir lectura_anterior, lectura_actual, costo_por_kilovatio, consumo, monto_total Como Real
	
    Escribir "Ingrese la lectura anterior del contador (en kilovatios): "
    Leer lectura_anterior
    Escribir "Ingrese la lectura actual del contador (en kilovatios): "
    Leer lectura_actual
    Escribir "Ingrese el costo por kilovatio: "
    Leer costo_por_kilovatio
	
    // Caja negra
    consumo = lectura_actual - lectura_anterior
	monto_total = consumo * costo_por_kilovatio
	
    // Salidas
    Escribir "El monto total a pagar por la luz eléctrica es: ", monto_total
FinAlgoritmo
