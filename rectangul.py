from math import fabs

class Rectangulo:
    
    def __init__(self, punto1=None, punto2=None):
        if punto1 is None:
            punto1 = Punto(0,0)
        if punto2 is None:
            punto2 = Punto(0,0)
        self.punto1 = punto1
        self.punto2 = punto2
        
    def base(self):
        return fabs(self.punto2.x - self.punto1.x)
    
    def altura(self):
        return fabs(self.punto2.y - self.punto1.y)
    
    def area(self):
        return self.base() * self.altura()
