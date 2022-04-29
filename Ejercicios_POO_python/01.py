class Persona:
    def setNombre(self,nom):
        self.nombre=nom

    def imprimir(self):
        print("Nombre: ",self.nombre)



persona=Persona()
persona.setNombre("Nacho")
persona.imprimir()