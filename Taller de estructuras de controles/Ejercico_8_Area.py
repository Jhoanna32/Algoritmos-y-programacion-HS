#Calcule el área de un triángulo en función de las longitudes de sus lados, utilizan la fórmula:
datosa=int(input("ingrese la datos de a:"))
datosb=int(input("ingrese la datos de b:"))
datosc=int(input("ingrese la datos de c:"))

datosSeriperimetro=(datosa+datosb+datosc)/2
resultado=(datosSeriperimetro*(datosSeriperimetro-datosa)*(datosSeriperimetro-datosb)*(datosSeriperimetro-datosc))
area= (resultado**0.5)

print(f"los datos del seriperimetro es: {datosSeriperimetro}" )
print(f"los datos del area es:  {area}")