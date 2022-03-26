def contar_vocales(frase):
    cantVocales = 0
    for i in frase:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            cantVocales += 1
        
    print(cantVocales)

contar_vocales("lorem ipsum")