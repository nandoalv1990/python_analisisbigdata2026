#Clase calculadora

class Calculadora:
    def __init__(self, numero1:float, numero2:float):
        self.n1 = numero1
        self.n2 = numero2

    def suma(self) -> float:
        return print(self.n1, " + ", self.n2, " = ", self.n1 + self.n2)
    def multi(self) -> float:
        return print(self.n1, " X ", self.n2, " = ", self.n1 * self.n2)
    def resta(self) -> float:
        return print(self.n1, " - ", self.n2, " = ", self.n1 - self.n2)
    def divi(self) -> float:
        try:
            return print(self.n1, " / ", self.n2, " = ", self.n1 / self.n2)
        except:
            print("No se puede dividir entre cero")
            return None

n1=float(input(":"))
n2=float(input(":"))
operacion = Calculadora(n1, n2)

operacion.suma()
operacion.resta()
operacion.multi()
operacion.divi()