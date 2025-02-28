#Dados los datos A, B, C y D que representan números enteros; escriba un algoritmo que calcule el resultado de las siguientes expresiones:
n=input()
a=int(input("Ingresar valor de A: "))
b=int(input("Ingresar el valor de B: "))
c=int(input("Ingresar el valor de C: "))
d=int(input("Ingresar el valor de D: "))

if d==0:
    print((a-c)**2)
elif d>0:
    print(((a-b)**3)/d)