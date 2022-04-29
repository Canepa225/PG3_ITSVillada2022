class Triangulo:
    def inicializar(self):
        self.lado1 = input("Introduzca el lado 1: ")
        self.lado2 = input("Introduzca el lado 2: ")
        self.lado3 = input("Introduzca el lado 3: ")

    def imprimirMayor(self):
        if self.lado1 > self.lado2 and self.lado1 > self.lado3:
            print("El mayor es: ", self.lado1)
        elif self.lado2 > self.lado1 and self.lado2 > self.lado3:
            print("El mayor es: ", self.lado2)
        else:
            print("El mayor es: ", self.lado3)

    def esEquilatero(self):
        if self.lado1 == self.lado2 and self.lado2 == self.lado3:
            print("Es equilatero")
        else:
            print("No es equilatero")

triangulo1 = Triangulo()
triangulo1.inicializar()
triangulo1.imprimirMayor()
triangulo1.esEquilatero()