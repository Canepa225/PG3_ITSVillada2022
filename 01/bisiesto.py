def es_bisiesto(año):
    if((año % 400 == 0) or (año % 100 != 0) and (año % 4 == 0)):
        print(año,"es bisiestio.")
    else:
        print(año,"no es bisiesto.")

list = [2012, 2010, 2000, 1900]
for x in list:
    es_bisiesto(x)
