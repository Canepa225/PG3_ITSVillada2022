try:
    with open('ej_5.txt', 'w') as archivo:
        archivo.write(0)
except TypeError:
    print("Error: Solo se puede ingresar strings.")
    