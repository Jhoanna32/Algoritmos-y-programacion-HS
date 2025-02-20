#10.	El cambio de divisas en la bolsa de Madrid el 25/08/1987 fue el siguiente 100 chelines austríacos	=	956.871 pesetas
#1 dólar EEUU	=	122.499 pesetas
#100 dracmas griegos =	88.607 pesetas
#100 francos belgas	=	323.728 pesetas
#1 franco francés	=	20.110 pesetas
#1 libra esterlina	=	178.938 pesetas
#100 liras italianas	=	9.289 pesetas
#Lea una cantidad en chelines austriacos e imprima el equivalente en pesetas. Lea una cantidad en dracmas griegos e imprima su equivalente en francos franceses. Finalmente, lea una cantidad en pesetas e imprima su equivalente en dólares y liras italianas.

chelines=int(input("ingrese la cantidad de chelines:  "))
dracmas=int(input("ingrese la cantidad de dracmas:  "))
pecetas=int(input("ingrese la cantidad de pecetas:  "))
#caja negra 
chelines1=(chelines*956.781)/100
pecetas1=(dracmas*88.607)/100
francos=(pecetas1/20.110)
dolares=(pecetas/122.499)
liras=(pecetas*100)/9.289
#salida
print(f"la cantidad de chelines a pecetas es:  {chelines}")
print(f"la cantidad de dragmas a francos es:  {francos}")
print(f"la cantidad equivalente al dolar es:n  {dolares}")
print(f"la cantidadd de liras equivalentes es:  {liras}")