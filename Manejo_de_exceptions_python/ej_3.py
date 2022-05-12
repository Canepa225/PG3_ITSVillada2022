tupla_meses = ("enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre")

while True:
    try:
        mes = int(input("Ingrese el numero de un mes (1-12): "))
        print("El mes ingresado es:", tupla_meses[mes - 1])
        break

    except ValueError:
        print("El valor ingresado no es valido.")


