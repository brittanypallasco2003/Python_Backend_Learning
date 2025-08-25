# Programa que me diga si un año es bisiesto
import calendar
from datetime import datetime


def main():
    print("¿Es un año bisiesto?")
    while True:
        option = input(""" Ingrese cualquiera de los literales para continuar:
            a) Conocer si el año actual es bisiesto
            b) Conocer si cualquier año es bisiesto
                    """)
        if option not in {"a", "b"}:
            print("Error la opción no es válida\n")
            continue
        if option == "a":
            year = datetime.now().year
        else:
            try:
                year = int(input("Ingrese el año para verificar si es bisiesto: "))
            except ValueError:
                print("Error: Debe ingresar un número válido \n")
                continue
        message = f"El año {year} {'es' if is_year_leap(year) else 'no es'} bisiesto"
        print(message)
        break


def is_year_leap(year):
    return calendar.isleap(year)


main()
