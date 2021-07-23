class Calculadora:
    def __init__(self, numero1, numero2):
        self.nu1 = numero1
        self.nu2 = numero2 

    def suma(self):
        return self.nu1 + self.nu2
    
    def resta(self):
        pass

    def multiplicacion (self):
        multi = self.nu1 * self.nu2
        print("{} * {} = {}".format(self.nu1,self.nu2, multi)) 
    
    def division (self):
        pass

class CalEstandar(Calculadora):
    def __init__(self, numero1, numero2):
        super().__init__(numero1, numero2) 
    def multiplicacion(self):
        return self.nu1 * self.nu2 
    def exponente(self):
        pass 
    def valorAbsoluto(self,numero): 
        if numero < 0 :
            numero = numero*1
        return numero 
class CalCientifica(Calculadora):
    def __init__(self, numero1, numero2):
        super().__init__(numero1, numero2) 
# cal = Calculadora (4,7) 
# cal.multiplicacion() 
calEst= CalEstandar(4,7) 
print(calEst.multiplicacion())