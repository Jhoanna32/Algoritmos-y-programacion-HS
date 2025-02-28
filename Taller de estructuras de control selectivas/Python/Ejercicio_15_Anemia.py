#Tomando como base los resultados obtenidos en un laboratorio de análisis clínicos, un médico determina si una persona tiene anemia o no, lo cual depende de su nivel de hemoglobina en la sangre, de su edad y de su sexo. Si el nivel de hemoglobina que tiene una persona es menor que el rango que le corresponde, se determina su resultado como positivo y en caso contrario como negativo. La tabla en la que el médico se basa para obtener el resultado es la siguiente:

def determinar_anemia(edad, nivel_hemoglobina, sexo):
    if edad <= 1/12:
        rango_min, rango_max = 13, 26
    elif 1/12 < edad <= 6/12:
        rango_min, rango_max = 10, 18
    elif 6/12 < edad <= 1:
        rango_min, rango_max = 11, 15
    elif 1 < edad <= 5:
        rango_min, rango_max = 11.5, 15
    elif 5 < edad <= 10:
        rango_min, rango_max = 12.6, 15.5
    elif 10 < edad <= 15:
        rango_min, rango_max = 13, 15.5
    elif sexo == 'mujer' and edad > 15:
        rango_min, rango_max = 12, 16
    elif sexo == 'hombre' and edad > 15:
        rango_min, rango_max = 14, 18
    else:
        return "Datos inválidos"

    if nivel_hemoglobina < rango_min:
        return "Positivo para anemia"
    else:
        return "Negativo para anemia"

def main():
    try:
        edad = float(input("Ingrese la edad en años (por ejemplo, 0.5 para 6 meses): "))
        nivel_hemoglobina = float(input("Ingrese el nivel de hemoglobina en g/dl: "))
        sexo = input("Ingrese el sexo (hombre/mujer): ").strip().lower()

        resultado = determinar_anemia(edad, nivel_hemoglobina, sexo)
        print(f"Resultado: {resultado}")

    except ValueError:
        print("Por favor, ingrese valores numéricos válidos para la edad y el nivel de hemoglobina.")

if __name__ == "__main__":
    main()
