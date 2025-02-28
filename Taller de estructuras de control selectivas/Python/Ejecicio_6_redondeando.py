#Se tienen 4 dígitos en las variables A, B, C, D que forman un entero positivo N. Se desea redondear N a la centena más próxima y mostrar el resultado. Considere los siguientes ejemplos: Si A es 2, B es 3, C es 6 y D es 2, entonces N es 2362 y el resultado redondeado es 2400. Si N es 2342, el resultado redondeado será 2300 y si N es 2962, el resultado redondeado será 3000.

def redondear_a_centena_mas_proxima(a, b, c, d):
    n = int(f"{a}{b}{c}{d}")
    redondeado = round(n, -2)
    return redondeado

a = int(input("Ingrese el valor de A: "))
b = int(input("Ingrese el valor de B: "))
c = int(input("Ingrese el valor de C: "))
d = int(input("Ingrese el valor de D: "))

resultado = redondear_a_centena_mas_proxima(a, b, c, d)

print(f"El número redondeado a la centena más próxima es: {resultado} COP")
