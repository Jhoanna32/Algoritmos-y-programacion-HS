#Desarrolle un algoritmo, que dado como dato una temperatura en grados Fahrenheit, determine el deporte que es apropiado practicar a esa temperatura, teniendo en cuenta la siguiente tabla:

def determinar_deporte(temperatura):
    if temperatura > 85:
        deporte = "Natación"
    elif 70 < temperatura <= 85:
        deporte = "Tenis"
    elif 32 < temperatura <= 70:
        deporte = "Golf"
    elif 10 < temperatura <= 32:
        deporte = "Esquí"
    else:
        deporte = "Marcha"
    return deporte

temperatura = float(input("Ingrese la temperatura en grados Fahrenheit: "))

deporte = determinar_deporte(temperatura)

print(f"El deporte apropiado para practicar a {temperatura:.2f} grados Fahrenheit es: {deporte}")
