from mimetypes import init


class Operaciones:
    def __init__(self):
        self.num1 = int(input("Introduzca el primer numero: "))
        self.num2 = int(input("Introduzca el segundo numero: "))
        self.suma()
        self.resta()
        self.multiplicacion()
        self.division()

    def suma(self):
        print("suma: ",self.num1 + self.num2)

    def resta(self):
        print("resta: ",self.num1 - self.num2)

    def multiplicacion(self):
        print("multiplicación: ",self.num1 * self.num2)

    def division(self):
        print("division: ",self.num1 / self.num2)

operacion = Operaciones()