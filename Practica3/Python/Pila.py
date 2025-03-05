class Pila:
    def __init__(self, n):
        self.__arreglo = ([0] * n)
        self.__top = -1
        self.__n = n

    def push(self, e):
        if self.isFull():
            print("La pila está llena")
        self.__top += 1
        self.__arreglo[self.__top] = e

    def pop(self):
        if self.isEmpty():
            print("La pila está vacía")
        elemento = self.__arreglo[self.__top]
        self.__top -= 1
        return elemento

    def peek(self):
        if self.isEmpty():
            print("La pila está vacía")
        return self.__arreglo[self.__top]

    def isEmpty(self):
        return self.__top == -1

    def isFull(self):
        return self.__top == self.__n - 1


pila = Pila(5)
pila.push(10)
pila.push(20)
pila.push(30)
pila.push(40)
print(pila.pop())
print(pila.pop())
print(pila.pop())
print(pila.peek())
