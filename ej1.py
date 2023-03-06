import math

class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return "({},{})".format(self.x, self.y)
    
    def cuadrante(self):
        if self.x > 0 and self.y > 0:
            return "El punto {} pertenece al primer cuadrante".format(self)
        elif self.x < 0 and self.y > 0:
            return "El punto {} pertenece al segundo cuadrante".format(self)
        elif self.x < 0 and self.y < 0:
            return "El punto {} pertenece al tercer cuadrante".format(self)
        elif self.x > 0 and self.y < 0:
            return "El punto {} pertenece al cuarto cuadrante".format(self)
        elif self.x == 0 and self.y != 0:
            return "El punto {} se sitúa sobre el eje Y".format(self)
        elif self.x != 0 and self.y == 0:
            return "El punto {} se sitúa sobre el eje X".format(self)
        else:
            return "El punto {} está sobre el origen".format(self)
    
    def vector(self, otro_punto):
        dx = otro_punto.x - self.x
        dy = otro_punto.y - self.y
        return "El vector resultante entre {} y {} es ({},{})".format(self, otro_punto, dx, dy)
    
    def distancia(self, otro_punto):
        distancia = math.sqrt((otro_punto.x - self.x)**2 + (otro_punto.y - self.y)**2)
        return "La distancia entre los puntos {} y {} es {}".format(self, otro_punto, distancia)


# Crear un objeto de tipo Punto
p = Punto(3, 4)
print(p)

# Calcular el cuadrante al que pertenece el punto
print(p.cuadrante())

# Crear otro punto
q = Punto(-2, 1)

print(p.vector(q))
print(p.distancia(q))
