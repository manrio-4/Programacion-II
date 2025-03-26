class Estadistica:
    def __init__(self):
        self.datos = []
        self.cantidad = len(self.datos)
        
    def agregarDatos(self, dato):
        self.datos.append(dato)
        self.cantidad = self.cantidad+1
    
    def promedio(self):
        suma = 0
        for i in range(self.cantidad):
            suma = suma + self.datos[i]
        promedio = suma / self.cantidad
        return promedio
    def desviacionEstandar(self):
        desv = 0
        for i in range(self.cantidad):
            desv = desv + (self.datos[i]-self.promedio())**2
        desv = desv/self.cantidad-1
        desv = desv**0.5
        return desv
    
class main():
    entrada = input()
    a, b, c, d, e, f, g, h, i, j = map(float, entrada.split())
    est = Estadistica()
    est.agregarDatos(a)
    est.agregarDatos(b)
    est.agregarDatos(c)
    est.agregarDatos(d)
    est.agregarDatos(e)
    est.agregarDatos(f)
    est.agregarDatos(g)
    est.agregarDatos(h)
    est.agregarDatos(i)
    est.agregarDatos(j)
    print(f"El promedio es:{est.promedio()}")
    print(f"La desviacion estandar es: {est.desviacionEstandar()}")