# pip install multimethod
from multimethod import multimethod
import math
from decimal import Decimal
class Area:
    @multimethod
    def area(self, radio: float):
        return math.pi * radio * radio #Circulo
    @multimethod
    def area(self, altura: float, base: float):
        return base * altura #Rectangulo
    @multimethod
    def area(self, altura: Decimal, base: Decimal):
        return (base * altura) / 2 #Triangulo Rectangulo
    @multimethod
    def area(self, baseMenor: float, baseMayor: float, altura:float):
        return ((baseMenor + baseMayor) * altura) / 2 #Trapecio

    @multimethod
    def area(self, perimetro: float, apotema: float):
        return (perimetro * apotema) / 2 #Pentagono
figura = Area()
f1 = figura.area(1.0)
f2 = figura.area(3.0, 4.0)
f3 = figura.area(Decimal("5.0"), Decimal("6.0"))
f4 = figura.area(3.0, 5.0, 4.0)
f5 = figura.area(10.0, 7.0)
print("Circulo:", f1)
print("Rectángulo:", f2)
print("Triángulo Rectángulo:", f3)
print("Trapecio:", f4)
print("Pentagono:", f5)