Algoritmo Ejercico_16_galones
	//Entradas
	Definir galones, litros, precio_por_litro, total Como Real
    Constante <- litro_por_galon = 3.785
    Constante <- precio_por_litro = 50000
    Escribir "Ingrese la cantidad de galones surtidos:"
    Leer galones
    
    // Caja negra
    litros = galones * litro_por_galon
    total = litros * precio_por_litro
    
    // Salidas
    Escribir "El total a cobrar es: ", total, " COP"
FinAlgoritmo
