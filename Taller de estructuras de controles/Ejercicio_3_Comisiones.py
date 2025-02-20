#Un vendedor recibe un sueldo base, más un 10% extra por comisiones de sus ventas. El vendedor desea saber cuánto dinero obtendrá por concepto de comisiones por las tres ventas que realizó en el mes y el total que recibirá tomando en cuenta su sueldo base y sus comisiones.
sueldo= int(input("Ingrese su sueldo base: "))
porcentaje_extra= 0.1
Venta1= int(input("Ingrese el valor de la venta uno:  ")) 
Venta2= int(input("Ingrese el valor de la venta dos:  ")) 
Venta3= int(input("Ingrese el valor de la venta tres:  ")) 
Venta_total= (Venta1+Venta2+Venta3)
Comision= (Venta_total*porcentaje_extra)
Sueldo_final= (sueldo+Comision)
print (f"Tu sueldo es: {sueldo} $")
print (f"Tu Comisión es: {Comision} $")
print (f"Tu sueldo a recibir es: {Sueldo_final} $")
