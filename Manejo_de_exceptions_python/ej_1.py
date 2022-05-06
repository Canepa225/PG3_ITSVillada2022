def sumar_numeros():
    try:
        numero1 = int(input("Introduce el primer número: "))
        numero2 = int(input("Introduce el segundo número: "))
        suma = numero1 + numero2
        print("La suma es: ",suma)
        while True:
            pregunta = input("¿Desea sumar más valores? (s/n): ")
            if pregunta == "s":
                num = int(input("Introduce el numero a sumar: "))
                suma += num
                print("La suma es: ",suma)
            else:
                break

    except ValueError:
        print("Error: Debes introducir números")
        while True:
            pregunta = input("¿Desea sumar más valores? (s/n): ")
            if pregunta == "s":
                num = int(input("Introduce el numero a sumar: "))
                suma += num
                print("La suma es: ",suma)
            else:
                break


sumar_numeros()
