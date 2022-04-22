def pintame():

    ancho = int(input("Ingrese ancho: "))
    alto = int(input("Ingrese alto: "))
    caracter = input("Ingrese caracter: ")

    option = input("¿Qué quieres pintar? Rectangulo(1) o Triangulo(2): ")
    if option == "1":
        for x in range(0, alto):
            print(caracter*ancho)
    elif option == "2":
        for fila in range(0, alto):
            print(" " * (alto-fila) + caracter * (2*fila - 1))

pintame()
