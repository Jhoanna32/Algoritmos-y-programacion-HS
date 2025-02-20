#Calcular el salario neto de un trabajador en función del número de horas trabajadas, el precio de la hora y considerando un descuento fijo al sueldo base por concepto de impuestos del 20%.
Horas_Trabajadas = int(input("Ingrese en total de horas trabajadas: "))
Precio_hora = float(input("Ingrese el precio de la hora: $" ))
Descuento = 0.2
Salario_Base = Horas_Trabajadas , Precio_hora
Salario_Neto = Salario_Base * Descuento
print(f"Su salario neto a recibir es: {Salario_Neto}")
