#Un maestro desea saber qué porcentaje de hombres y qué porcentaje de mujeres hay en un grupo de estudiantes
Hombres= int(input("Ingrese cantidad de hombres:  "))
Mujeres= int(input("Ingrese cantidad de mujeres:  "))
Total_estudiantes= (Hombres+Mujeres)
PorcentajeH= (Hombres/Total_estudiantes)*100
PorcentajeM= (Mujeres/Total_estudiantes)*100
print(f"El porcentaje de hombres es: {PorcentajeH} %")
print(f"El porcentaje de mujeres es: {PorcentajeM} %")