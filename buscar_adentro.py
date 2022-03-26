def buscar_adentro(list):
    print(list)
    num = int(input("Ingrese el numero que desee saber su ubicacion: "))
    print("La ubicacion del numero '",num,"' es:",list.index(num))

list = [8,4,7,2,0,3,1,6,5,9]
buscar_adentro(list)
