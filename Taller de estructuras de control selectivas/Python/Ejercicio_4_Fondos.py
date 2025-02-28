#Una empresa quiere hacer una compra de varias piezas de la misma clase a un fabricante de refacciones. La empresa dependiendo del monto total de la compra, decidirá qué hacer para pagar al fabricante. Si el monto total de la compra excede de $5.000.000 COP la empresa tendrá la capacidad de invertir de su propio dinero un 5 5 % del monto de la compra, pedir presta al banco un 30% y el resto lo pagará solicitando un crédito al fabricante. Si el monto total de la compra no excede de $5.000.000 COP la empresa tendrá capacidad de invertir de su propio dinero un 70% y el restante 30% lo pagará solicitando crédito al fabricante. El fabricante cobra por concepto de intereses un 20% sobre la cantidad que se le pague a crédito.   Calcule y muestre la cantidad a invertir de los fondos de la empresa, la cantidad a pagar a crédito, el monto a pagar por intereses y si es necesario, la cantidad prestada al banco.

def calcular_pagos(monto_total):
    if monto_total > 5000000:
        inversion_empresa = monto_total * 0.55
        prestamo_banco = monto_total * 0.30
        credito_fabricante = monto_total * 0.15
    else:
        inversion_empresa = monto_total * 0.70
        prestamo_banco = 0
        credito_fabricante = monto_total * 0.30

    intereses = credito_fabricante * 0.20

    return inversion_empresa, prestamo_banco, credito_fabricante, intereses

monto_total = float(input("Ingrese el monto total de la compra: "))

inversion_empresa, prestamo_banco, credito_fabricante, intereses = calcular_pagos(monto_total)

print(f"La cantidad a invertir de los fondos de la empresa es: {inversion_empresa:.2f} COP")
if prestamo_banco > 0:
    print(f"La cantidad a pagar solicitando un préstamo al banco es: {prestamo_banco:.2f} COP")
print(f"La cantidad a pagar a crédito al fabricante es: {credito_fabricante:.2f} COP")
print(f"El monto a pagar por intereses es: {intereses:.2f} COP")
