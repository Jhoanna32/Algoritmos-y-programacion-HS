#4.	Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuánto deberá pagar finalmente por su compra
Descuento= 0.15
Total_Compra= int(input("Ingresa el valor total de la compra:  "))
Pago= Total_Compra - (Total_Compra*Descuento)
print(f"Valor de la compra: {Total_Compra} $")
print(f"Valor a pagar con descuento es: {Pago} $")