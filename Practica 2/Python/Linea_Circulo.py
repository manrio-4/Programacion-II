import math

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
        return f"Línea entre {self.p1} y {self.p2}"


class Circulo:
    def __init__(self, centro: Punto, radio: float):
        self.centro = centro
        self.radio = radio

    def __str__(self):
        return f"Círculo con centro en {self.centro} y radio {self.radio}"


# 📌 Pruebas de las clases
p1 = Punto(3, 4)
p2 = Punto(10, 8)
linea = Linea(p1, p2)
centro = Punto(5, 5)
circulo = Circulo(centro, 7)

print(p1)
print(p1.coord_cartesianas())
print(p1.coord_polares())
print(linea)
print(circulo)
