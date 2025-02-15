Algoritmo Ejercicio_3_ventas
	// Entrada
    Definir sueldo_base, venta1, venta2, venta3, comision, total_comisiones, total_recibir Como Real
	
    Escribir "Ingrese el sueldo base del vendedor: "
    Leer sueldo_base
	
    Escribir "Ingrese el monto de la primera venta: "
    Leer venta1
    Escribir "Ingrese el monto de la segunda venta: "
    Leer venta2
    Escribir "Ingrese el monto de la tercera venta: "
    Leer venta3
	
    // Caja negra
    comision = 0.10
    total_comisiones = (venta1 + venta2 + venta3) * comision
    total_recibir = sueldo_base + total_comisiones
	
    // Salidas
    Escribir "El total de comisiones por las tres ventas es: ", total_comisiones
    Escribir "El total que recibirá el vendedor, incluyendo el sueldo base, es: ", total_recibir
FinAlgoritmo
