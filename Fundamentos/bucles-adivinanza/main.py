# Adivina el número

import random


def main():
    print("Bienvenido a adivina el número")
    while True:
        option = (
            input("""\nIngrese cualquiera de los literales para continuar:\n
        a) Adivinar un número par o impar entre el rango seleccionado
        b) Adivinar un número par o impar por un rango ya establecido 0-20: 
        Opción: """)
            .strip()
            .lower()
        )

        if option == "a":
            random_value = generar_valor_personalizado()
            pass

        elif option == "b":
            random_value = asignar_valor_aleatorio(0, 20)
            pass
        else:
            print("Opción inválida, intenta de nuevo.\n")
            continue

        jugar(random_value)

        break


def asignar_valor_aleatorio(start, end):
    return random.randint(start, end)


def generar_valor_personalizado():
    while True:
        try:
            start = int(input("Ingrese el valor inicial del rango: "))
            end = int(input("Ingrese el valor final del rango: "))
            if start >= end:
                print("El valor final no puede ser menor o igual que el inicial")
                continue
            return asignar_valor_aleatorio(start, end)
        except ValueError:
            print("Entrada inválida. Debe ingresar números enteros\n")


def jugar(random_value):
    while True:
        try:
            num_ingresado = int(
                input(
                    "Intente adivinar el número ingresando un número entero teniendo en cuenta los rangos establecidos: "
                )
            )
            if num_ingresado == random_value:
                print("Felicidades, le atinaste")
                break
            else:
                print("Fallaste. Inténtalo de nuevo\n")
        except ValueError:
            print("Entrada inválida. Debe ingresar números enteros")
            continue


main()
