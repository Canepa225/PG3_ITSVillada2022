def dividir_numeros():
    try:
        numero1 = int(input("Introduce el primer número: "))
        numero2 = int(input("Introduce el segundo número: "))
        division = numero1 / numero2
        print("La división es: ",division)
        
    except ZeroDivisionError:
        print("Error: No se puede dividir entre 0")

dividir_numeros()