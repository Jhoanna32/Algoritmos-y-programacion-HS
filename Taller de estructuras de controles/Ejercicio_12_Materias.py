#Calcule y muestre, a un alumno, cuál será su promedio general en las tres materias más difíciles que cursa y cuál será el promedio que obtendrá en cada una de ellas. Estas materias se evalúan como se muestra a continuación:
#Matemática		Examen 90% y	10% del promedio de tres tareas.
#Física		Examen 80% y	20% del promedio de dos tareas.
#Química		Examen 85% y	15% del promedio de tres tareas.


examenM=float(input("introduzca el valor de su examen de matematicas:  "))
taream1=float(input("introduzca la primera nota de la tarea de matematica:  "))
taream2=float(input("introduzca la segunda nota de la tarea de matematica:  "))
taream3=float(input("introduzca la tercera nota de la tarea de matematicas:  "))
examenF=float(input("introduzca a nota de el examen de fisica:  "))
tareaf1=float(input("introduzca la nota de la primera tarea de fisica:  "))
tareaf2=float(input("introduzca la nota de la segunda tarea de fisica:  "))
examenQ=float(input("introduzca la nota de el examen de quimica:  "))
tareaq1=float(input("introduzca la nota de la primera tarea de quimica:  "))
tareaq2=float(input("introduzca la nota de la segunda tarea de quimica:  "))
tareaq3=float(input("introduzca la nota de la tercera tarea de quimica:  "))
notam1=(examenM*0.90)
notam2=(taream1+taream2+taream3)*0*10
notam3=(notam1+notam2)
notaf1=(examenF*0.80)
notaf2=(tareaf1+tareaf2)*0.20
notaf3=(notaf1+notaf2)
notaq1=(examenQ*0.85)
notaq2=(tareaq1+tareaq2+tareaq3)*0.15
notaq3=(notaq1+notaq2)
print(f"la nota de matematicas con sus respectivos porcentajes es:  {notam3}")
print(f"la nota de fisica con sus respectivos porcentajes es de:  {notaf3}")
print(f"la nota de quimica con sus respectivos porcentajes es de:  {notaq3}")