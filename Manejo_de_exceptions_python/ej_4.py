def dividir_numeros():
    while True:
        try:
            numero1 = int(input("Introduce el primer número: "))
            numero2 = int(input("Introduce el segundo número: "))
            division = numero1 / numero2
            print("La división es: ",division)
            break
        
        except ZeroDivisionError:
            print("Error: No se puede dividir entre 0")
        except ValueError:
            print("Error: El valor ingresado no es valido.")

dividir_numeros()