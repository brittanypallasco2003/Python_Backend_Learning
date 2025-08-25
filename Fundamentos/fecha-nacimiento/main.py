# Función que recibe tu fecha de nacimiento y devuelve tu edad.
from datetime import datetime


def main():
    while True:
        print("CALCULADORA DE EDAD")
        fecha_nacimiento = input("""
Ingrese su fecha de nacimiento con cualquiera de los siguientes formatos:
          - DD/MM/AAAA
          - DD-MM-AAAA
          """)
        try:
            edad = devolver_edad(fecha_nacimiento)
            print(f"Su edad actual es: {round(edad)}")
            break
        except (ValueError, TypeError) as error:
            print(f"Error: {error}. Inténtelo de nuevo.\n")


def devolver_edad(fecha_nacimiento):
    hoy = datetime.now()
    if "/" in fecha_nacimiento:
        fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%d/%m/%Y")
    elif "-" in fecha_nacimiento:
        fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%d-%m-%Y")

    if fecha_nacimiento > hoy:
        raise ValueError("La fecha de nacimiento no puede ser futura")

    intervalo_tiempo = hoy - fecha_nacimiento
    return intervalo_tiempo.days / 365


main()
