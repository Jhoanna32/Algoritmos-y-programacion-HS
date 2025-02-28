#en una tienda efectúan un descuento a los clientes dependiendo del monto de la compra. El descuento se efectúa con base en el siguiente criterio:
#a.	Si el monto es inferior a $50.000 COP, no hay descuento.
#b.	Si está comprendido entre $50.000 COP y $100.000 COP inclusive, se hace un descuento del 5%
#c.	Si está comprendido entre $100.000 COP y $700.000 COP inclusive, se hace un descuento del 11%
#d.	Si está comprendido entre $700.000 COP y $1.500.000 COP inclusive, el descuento es del 18
#e.	Si el monto es mayor a $1.500.000., hay un 25% de descuento.
#Calcule y muestre el nombre del cliente, el monto de la compra, monto a pagar y descuento recibido.

def calcular_descuento(monto_compra):
    if monto_compra < 50000:
        descuento = 0
    elif monto_compra <= 100000:
        descuento = 0.05
    elif monto_compra <= 700000:
        descuento = 0.11
    elif monto_compra <= 1500000:
        descuento = 0.18
    else:
        descuento = 0.25

    monto_descuento = monto_compra * descuento
    monto_pagar = monto_compra - monto_descuento
    
    return monto_descuento, monto_pagar

nombre_cliente = input("Ingrese el nombre del cliente: ")
monto_compra = float(input("Ingrese el monto de la compra (en COP): "))

monto_descuento, monto_pagar = calcular_descuento(monto_compra)

print(f"Nombre del cliente: {nombre_cliente}")
print(f"Monto de la compra: {monto_compra:.2f} COP")
print(f"Descuento recibido: {monto_descuento:.2f} COP")
print(f"Monto a pagar: {monto_pagar:.2f} COP")

