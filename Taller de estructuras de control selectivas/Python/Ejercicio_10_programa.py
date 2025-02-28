#Construya un programa en Python que, dados como datos la categoría y el sueldo bruto del trabajador, calcule el aumento correspondiente teniendo en cuenta la siguiente tabla:

def calcular_aumento(categoria, sueldo_bruto):
    if categoria == 1:
        aumento = 0.10
    elif categoria == 2:
        aumento = 0.15
    elif categoria == 3:
        aumento = 0.20
    elif categoria == 4:
        aumento = 0.40
    elif categoria == 5:
        aumento = 0.60
    else:
        aumento = 0
        print("Categoría no válida")
    
    nuevo_sueldo_bruto = sueldo_bruto * (1 + aumento)
    return nuevo_sueldo_bruto

categoria = int(input("Ingrese la categoría del trabajador (1-5): "))
sueldo_bruto = float(input("Ingrese el sueldo bruto del trabajador (en COP): "))

nuevo_sueldo_bruto = calcular_aumento(categoria, sueldo_bruto)

print(f"La categoría del trabajador es: {categoria}")
print(f"El nuevo sueldo bruto del trabajador es: {nuevo_sueldo_bruto:.2f} COP")

