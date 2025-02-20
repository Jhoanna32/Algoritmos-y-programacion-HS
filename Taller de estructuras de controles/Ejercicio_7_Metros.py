#Dada una cantidad en metros, se requiere que la convierta a pies y pulgadas, considerando lo siguiente: 1 metro = 39.27 pulgadas; 1 pie = 12 pulgadas.
Metros=float(input("ingresa los metros que deseas convertir a pies y a pulgadas:  "))
pulgadas= round((Metros*39.27),2)
pies=(pulgadas/12)
print(f"La conversión en pulgadas es: {pulgadas}")
print(f"La conversión en pies es: {pies}")