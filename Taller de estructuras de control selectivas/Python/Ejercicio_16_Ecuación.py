#Confeccionar un algoritmo que permita resolver una ecuación de segundo grado, de la forma: AX2+BX+C = 0, sabiendo que el discriminante (D) se calcula con la fórmula: D= Bˆ2­4*A*C. El valor obtenido se evalúa y se aplica la fórmula correspondiente, según muestra la siguiente tabla:

import math

def resolver_ecuacion_segundo_grado(a, b, c):
    discriminante = b**2 - 4*a*c
    
    if discriminante > 0:
        x1 = (-b + math.sqrt(discriminante)) / (2*a)
        x2 = (-b - math.sqrt(discriminante)) / (2*a)
        return f"X1 = {x1}, X2 = {x2}"
    elif discriminante == 0:
        x = -b / (2*a)
        return f"X1 = X2 = {x}"
    else:
        return "No tiene solución en los Reales."

def main():
    a = float(input("Ingrese el valor de A: "))
    b = float(input("Ingrese el valor de B: "))
    c = float(input("Ingrese el valor de C: "))
    resultado = resolver_ecuacion_segundo_grado(a, b, c)
    print(f"Resultado: {resultado}")

if __name__ == "__main__":
    main()
