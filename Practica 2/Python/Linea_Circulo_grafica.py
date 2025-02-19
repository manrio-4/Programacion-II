import math
#Debemos instalar la libreria con: pip install matplotlib
import matplotlib.pyplot as plt

class Punto:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def coord_cartesianas(self):
        return f"Coordenadas Cartesianas: ({self.x}, {self.y})"

    def coord_polares(self):
        r = math.sqrt(self.x**2 + self.y**2)
        theta = math.atan2(self.y, self.x)
        return f"Coordenadas Polares: (r={r:.2f}, θ={math.degrees(theta):.2f}°)"

    def __str__(self):
        return f"Punto({self.x}, {self.y})"

class Linea:
    def __init__(self, p1: Punto, p2: Punto):
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        return f"Línea formada por {self.p1} y {self.p2}"

    def dibujaLinea(self):
        plt.plot([self.p1.x, self.p2.x], [self.p1.y, self.p2.y], marker='o', color='b', linestyle='-')
        plt.xlim(min(self.p1.x, self.p2.x) - 1, max(self.p1.x, self.p2.x) + 1)
        plt.ylim(min(self.p1.y, self.p2.y) - 1, max(self.p1.y, self.p2.y) + 1)
        plt.xlabel("Eje X")
        plt.ylabel("Eje Y")
        plt.title("Dibujo de Línea")
        plt.grid()
        plt.show()

class Circulo:
    def __init__(self, centro: Punto, radio: float):
        self.centro = centro
        self.radio = radio

    def __str__(self):
        return f"Círculo con centro en {self.centro} y radio {self.radio}"

    def dibujaCirculo(self):
        fig, ax = plt.subplots()
        circulo = plt.Circle((self.centro.x, self.centro.y), self.radio, color='r', fill=False)
        ax.add_patch(circulo)
        plt.xlim(self.centro.x - self.radio - 1, self.centro.x + self.radio + 1)
        plt.ylim(self.centro.y - self.radio - 1, self.centro.y + self.radio + 1)
        plt.xlabel("Eje X")
        plt.ylabel("Eje Y")
        plt.title("Dibujo de Círculo")
        plt.gca().set_aspect('equal', adjustable='box')
        plt.grid()
        plt.show()

# Ejemplo de uso
punto1 = Punto(2, 3)
punto2 = Punto(8, 7)
linea = Linea(punto1, punto2)

centro = Punto(5, 5)
circulo = Circulo(centro, 3)

print(linea)  # ➝ Línea formada por Punto(2, 3) y Punto(8, 7)
linea.dibujaLinea()  # ➝ Dibuja la línea

print(circulo)  # ➝ Círculo con centro en Punto(5, 5) y radio 3
circulo.dibujaCirculo()  # ➝ Dibuja el círculo
