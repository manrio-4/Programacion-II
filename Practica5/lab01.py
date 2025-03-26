#Mario Andres Covarrubias Espinoza
class EcuacionCuadratica:
    def __init__(self, a,b,c):
        self.__a = a
        self.__b = b
        self.__c = c
    
    def getDiscriminante(self):
        discriminante = (self.__b**2)-(4*self.__a*self.__c)
        return discriminante
    def getRaiz1(self):
        raiz = ((self.__b*(-1))+((self.getDiscriminante())**0.5))/(2*self.__a)
        return raiz
    def getRaiz2(self):
        raiz = ((self.__b*(-1))-((self.getDiscriminante())**0.5))/(2*self.__a)
        return raiz
    def solucion(self):
        if(self.getDiscriminante() >0):
            return (f"la ecuacion tiene dos raices: {self.getRaiz1()} y {self.getRaiz2()}")
        elif(self.getDiscriminante() == 0):
            return (f"la ecuacion tiene una raiz: {self.getRaiz1()}")
        else:
            return "La ecuacion no tiene raices reales"
      
def getDiscriminante(a,b,c):
        discriminante = (b**2)-(4*a*c)
        return discriminante        
class main():
    #solucion orientada a objetos
    entrada = input("Ingrese a,b,c:")
    a, b, c = map(float, entrada.split())
    ec01 = EcuacionCuadratica(a,b,c)
    ec02 = EcuacionCuadratica(2,3,6)
    print (ec01.solucion())  
    
    #Solucion modular
    entrada = input("Ingrese a,b,c:")
    a, b, c = map(float, entrada.split())
    print(getDiscriminante(a,b,c))
    
