def numero_step(num):
    num = str(num)
    numAnterior = int(num[0])
    primerNum = True
    for i in str(num):
        if primerNum != True:
            if int(i)+1 != numAnterior or int(i)-1 != numAnterior:
                return False
            else:
                numAnterior = i
            primerNum = False        
        return True

respuesta = numero_step(976787654)
 
if respuesta == True:
    print("True")
else:
    print("False")