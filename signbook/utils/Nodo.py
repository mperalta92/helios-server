
class Nodo:
    def __init__(self, val, izq = None, der = None):
        self.element = val
        self.izq = izq
        self.der = der
        self.altura = None

    def getElement(self):
        return self.element
    def getIzq(self):
        return self.izq
    def getDer(self):
        return self.der

    def getAltura(self):
        if self.izq == None and self.der == None:
            self.altura = 0
        elif self.altura == None:
            self.altura = 1 + max(self.izq.getAltura(), self.der.getAltura())
        return self.altura

    def setIzq(self, i):
        self.izq = i

    def setDer(self, d):
        self.der = d

    def setElement(self, e):
        self.element = e

