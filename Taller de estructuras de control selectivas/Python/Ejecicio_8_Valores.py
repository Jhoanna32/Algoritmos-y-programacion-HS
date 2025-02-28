#Dados como datos los valores enteros P y Q, determine si los mismos satisfacen la siguiente expresión: P3 + Q4 – 2*P2 > 680. En caso afirmativo debe mostrar los valores de “P y Q satisfacen la expresión”, de lo contrario muestre un mensaje “P y Q no Satisfacen la expresión”. Utilice la concatenación para mostrar los valores

def evaluar_expresion(p, q):
    expresion = p**3 + q**4 - 2*p**2
    if expresion > 680:
        return f"P = {p} y Q = {q} satisfacen la expresión."
    else:
        return f"P = {p} y Q = {q} no satisfacen la expresión."

p = int(input("Ingrese el valor de P: "))
q = int(input("Ingrese el valor de Q: "))

resultado = evaluar_expresion(p, q)

print(resultado)
