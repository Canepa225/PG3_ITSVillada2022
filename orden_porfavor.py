def ordenar_lista(list):
    print(list)
    n = len(list)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if list[j] < list[j + 1] :
                list[j], list[j + 1] = list[j + 1], list[j]
    print(list)


list = [8,4,7,2,0,3,1,6,5,9]
ordenar_lista(list)