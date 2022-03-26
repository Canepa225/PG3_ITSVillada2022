def pintame():
    ancho = int(input("Ingrese ancho: "))
    alto = int(input("Ingrese alto: "))
    caracter = input("Ingrese caracter: ")

    for x in range(0, alto):
        print(caracter*ancho)

pintame()
