Algoritmo Ejercicio_6_Mujeres_Hombres
	// Entradas
    Definir hombres, mujeres, total_estudiantes, porcentaje_hombres, porcentaje_mujeres Como Real
    Escribir "Ingrese la cantidad de hombres: "
    Leer hombres
    Escribir "Ingrese la cantidad de mujeres: "
    Leer mujeres
	
    // Caja negra
    total_estudiantes = hombres + mujeres
    porcentaje_hombres = (hombres / total_estudiantes) * 100
    porcentaje_mujeres = (mujeres / total_estudiantes) * 100
	
    // Salidas
    Escribir "El porcentaje de hombres en el grupo es: ", porcentaje_hombres, "%"
    Escribir "El porcentaje de mujeres en el grupo es: ", porcentaje_mujeres, "%"
FinAlgoritmo
