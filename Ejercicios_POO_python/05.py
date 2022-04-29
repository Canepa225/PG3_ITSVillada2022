class Persona:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
    
    def imprimir(self):
        print("Nombre: ",self.nombre)
        print("Edad: ",self.edad)


class Empleado(Persona):
    def __init__(self,nombre,edad,sueldo):
        super().__init__(nombre,edad)
        self.sueldo=sueldo
    
    def imprimir(self):
        super().imprimir()
        print("Sueldo: ",self.sueldo)

    def paga_impuestos(self):
        if self.sueldo>3000:
            print("Debe pagar impuestos")
        else:
            print("No paga impuestos")

persona1=Persona("Nacho",17)
persona1.imprimir()
print('\n')

empleado1=Empleado("Tomas",17,3100)
empleado1.imprimir()
empleado1.paga_impuestos()