#Un alumno desea saber cuál será su calificación final en la materia de computación.  Dicha calificación se compone de los siguientes porcentajes:  55% del promedio de sus tres calificaciones parciales, 30% de la calificación del examen final y 15% de la calificación de un trabajo final.

Porcentaje1= 0.55
Parcial1= float(input("Ingrese la nota del primer parcial: "))
Parcial2= float(input("Ingrese la nota del segundo parcial: "))
Parcial3= float(input("Ingrese la nota del tercer parcial: "))
Promedio= (Parcial1+Parcial2+Parcial3)/3
Peso1= (Promedio*Porcentaje1)

Porcentaje2= 0.3
Examen= float(input("Ingrese la nota del examen final: "))
Peso2= (Examen*Porcentaje2)

Porcentaje3= 0.15
Trabajo= float(input("Ingrese la nota del trabajo final: "))
Peso3= (Trabajo*Porcentaje3)

Peso_final= round((Peso1+Peso2+Peso3),2)

print(f"Su nota final de la materia de computación es: {Peso_final}")
