#Desarrolle un programa en Python que calcule y muestre el monto que debe pagar ar suscriptor por concepto de consumo de luz eléctrica y servicio de aseo urbano. Dicho monto se calcula multiplicando la diferencia de la lectura anterior y la lectura actual por el costo de cada Kilovatio hora, según la siguiente escala:
#0 ­ 1004.600 COP/ Kwh
#101 ­ 30080.00 COP/ Kwh
#301 – 500 100.000 COP /Kwh
#501 – en Adelante 120.000 COP/ Khw

def calcular_monto_consumo(lectura_anterior, lectura_actual):
    consumo = lectura_actual - lectura_anterior
    monto = 0

    if consumo <= 100:
        monto = consumo * 4600
    elif 101 <= consumo <= 300:
        monto = 100 * 4600 + (consumo - 100) * 80000
    elif 301 <= consumo <= 500:
        monto = 100 * 4600 + 200 * 80000 + (consumo - 300) * 100000
    else:
        monto = 100 * 4600 + 200 * 80000 + 200 * 100000 + (consumo - 500) * 120000

    return monto

def main():
    lectura_anterior = int(input("Ingrese la lectura anterior del medidor: "))
    lectura_actual = int(input("Ingrese la lectura actual del medidor: "))
    monto = calcular_monto_consumo(lectura_anterior, lectura_actual)
    print(f"El monto a pagar por consumo de luz eléctrica es: {monto} COP")

if __name__ == "__main__":
    main()
