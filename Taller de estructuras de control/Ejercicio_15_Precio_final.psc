Algoritmo Ejercicio_15_Precio_final
	//Entradas
	Definir precio_final, pvp, descuento Como Real
    
    Escribir "Ingrese el precio final pagado:"
    Leer precio_final
    Escribir "Ingrese el precio de venta al público (PVP):"
    Leer pvp
    
    // Caja negra
    descuento = ((pvp - precio_final) / pvp) * 100
    
    // Salidas
    Escribir "El porcentaje de descuento aplicado es: ", descuento, "%"
FinAlgoritmo
