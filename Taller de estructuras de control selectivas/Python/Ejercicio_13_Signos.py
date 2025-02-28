#Desarrolle un algoritmo que reciba como dato de entrada la fecha de nacimiento de una persona y a continuación escriba el nombre del signo del zodiaco correspondiente; así como su edad. Considere la siguiente tabla de signos:
from datetime import datetime

def obtener_signo_zodiaco(fecha_nacimiento):
    dia, mes, año = map(int, fecha_nacimiento.split('/'))
    fecha = datetime(año, mes, dia)
    
    signos_zodiaco = [
        ("Capricornio", datetime(año, 1, 1), datetime(año, 1, 20)),
        ("Acuario", datetime(año, 1, 21), datetime(año, 2, 19)),
        ("Piscis", datetime(año, 2, 20), datetime(año, 3, 19)),
        ("Aries", datetime(año, 3, 21), datetime(año, 4, 20)),
        ("Tauro", datetime(año, 4, 21), datetime(año, 5, 21)),
        ("Géminis", datetime(año, 5, 22), datetime(año, 6, 21)),
        ("Cáncer", datetime(año, 6, 22), datetime(año, 7, 22)),
        ("Leo", datetime(año, 7, 23), datetime(año, 8, 23)),
        ("Virgo", datetime(año, 8, 24), datetime(año, 9, 22)),
        ("Libra", datetime(año, 9, 23), datetime(año, 10, 22)),
        ("Escorpión", datetime(año, 10, 23), datetime(año, 11, 21)),
        ("Sagitario", datetime(año, 11, 22), datetime(año, 12, 21)),
        ("Capricornio", datetime(año, 12, 22), datetime(año, 12, 31))
    ]
    
    for signo, inicio, fin in signos_zodiaco:
        if inicio <= fecha <= fin:
            return signo
    
    return None

def calcular_edad(fecha_nacimiento):
    dia, mes, año = map(int, fecha_nacimiento.split('/'))
    fecha_nacimiento = datetime(año, mes, dia)
    hoy = datetime.today()
    edad = hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
    return edad

def main():
    fecha_nacimiento = input("Ingrese su fecha de nacimiento (dd/mm/aaaa): ")
    signo = obtener_signo_zodiaco(fecha_nacimiento)
    edad = calcular_edad(fecha_nacimiento)
    
    if signo:
        print(f"Tu signo del zodiaco es {signo} y tu edad es {edad} años.")
    else:
        print("No se pudo determinar tu signo del zodiaco.")

if __name__ == "__main__":
    main()
