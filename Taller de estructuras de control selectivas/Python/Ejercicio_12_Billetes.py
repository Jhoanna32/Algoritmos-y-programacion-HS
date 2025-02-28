#Dada una cantidad entera de COP, desarrolle un algoritmo que permita desglosar dicha cantidad en los billetes y monedas de curso legal en el País. Recuerde que estos son: 

def desglosar_cantidad(cantidad):
    
    denominaciones = [100000, 50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100, 50]
    resultado = []

    cantidad = (cantidad // 50) * 50

    for denominacion in denominaciones:
        if cantidad >= denominacion:
            cantidad_denominacion = cantidad // denominacion
            cantidad %= denominacion
            resultado.append(f"{cantidad_denominacion} x {denominacion}")

    return resultado

cantidad = int(input("Ingrese la cantidad en COP: "))

desglose = desglosar_cantidad(cantidad)

print("Desglose de la cantidad:")
for item in desglose:
    print(item)
