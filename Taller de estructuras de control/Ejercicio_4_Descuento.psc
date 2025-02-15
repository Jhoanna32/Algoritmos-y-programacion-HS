Algoritmo Ejercicio_4_Descuento
	//Entrada
	Definir total_compra, descuento, total_a_pagar Como Real
    Escribir "Ingrese el total de la compra: "
    Leer total_compra
	
    // Caja negra
    descuento = total_compra * 0.15
    total_a_pagar = total_compra - descuento
	
    // Salida
    Escribir "El monto del descuento es: ", descuento
    Escribir "El total a pagar después del descuento es: ", total_a_pagar

FinAlgoritmo
