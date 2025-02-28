#Un hombre desea saber cuánto dinero se generará por concepto de intereses sobre la cantidad que tiene en inversión en el banco. El decidirá reinvertir los intereses siempre y cuando éstos excedan a $100.000 COP y en ese caso, desea saber cuánto dinero tendrá finalmente en su cuenta.

monto_inversion=float(input("Cantidad de dinero a invertir: "))
interes=float(input("Interes anual: "))
reinversion=monto_inversion*interes
if float(monto_inversion>100):
    print("La cantidad de dinero invertida es mayor a 100: ")
else:
    print("La cantidad de dinero no invertiva es igual a 0: ")
print (F"El interes anual es de: {reinversion} % ")