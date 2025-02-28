#Escriba un algoritmo, que dado como dato el sueldo de un trabajador, le aplique un aumento del 15% si su salario bruto es inferior a $900.000 COP y 12% en caso contrario. Imprima el nuevo sueldo del trabajador.

def calcular_nuevo_sueldo(sueldo_actual):
    if sueldo_actual < 900000:
        aumento = 0.15
    else:
        aumento = 0.12

    nuevo_sueldo = sueldo_actual * (1 + aumento)
    return nuevo_sueldo

sueldo_actual = float(input("Ingrese el sueldo actual del trabajador: "))

nuevo_sueldo = calcular_nuevo_sueldo(sueldo_actual)

print(f"El nuevo sueldo del trabajador es: {nuevo_sueldo:.2f} COP")
