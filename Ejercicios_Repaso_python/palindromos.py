from ast import Return


def palindromos(palabra):
    for i in range(0, int(len(palabra)/2)):
        if palabra[i] != palabra[len(palabra)-i-1]:
            return False
    return True
    

palabra = "neuquen"
respuesta = palindromos(palabra)
 
if (respuesta):
    print("True")
else:
    print("False")
palindromos(palabra)