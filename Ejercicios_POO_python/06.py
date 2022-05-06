class Familia:
    def __init__(self,padre,madre,hijos):
        self.padre=padre
        self.madre=madre
        self.hijos=hijos

    def __str__(self):
        return "Familia: \nPadre: {}\nMadre: {}\nHijos: {}".format(self.padre,self.madre,self.hijos)

familia1=Familia("Juan","Maria",["Pedro","Ana","José"])
print(familia1)