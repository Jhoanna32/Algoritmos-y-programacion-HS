Algoritmo Ejercicio_9_Sueldo
	// Entrada
    Definir horas_trabajadas, precio_por_hora, sueldo_bruto, descuento_impuestos, sueldo_neto Como Real
    Escribir "Ingrese el número de horas trabajadas: "
    Leer horas_trabajadas
    Escribir "Ingrese el precio por hora: "
    Leer precio_por_hora
	
    // Caja negra
    sueldo_bruto = horas_trabajadas * precio_por_hora
    descuento_impuestos = sueldo_bruto * 0.20
    sueldo_neto = sueldo_bruto - descuento_impuestos
	
    // Salida
    Escribir "El salario neto del trabajador es: ", sueldo_neto	
FinAlgoritmo
