from math import sqrt

class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return "({}, {})".format(self.x, self.y)
    
    def cuadrante(self):
        if self.x > 0 and self.y > 0:
            return 1
        elif self.x < 0 and self.y > 0:
            return 2
        elif self.x < 0 and self.y < 0:
            return 3
        elif self.x > 0 and self.y < 0:
            return 4
        else:
            return 0
        
    def vector(self, punto):
        return (punto.x - self.x, punto.y - self.y)
    
    def distancia(self, punto):
        return sqrt((punto.x - self.x)**2 + (punto.y - self.y)**2)

class Rectangulo:
    def __init__(self, punto1=None, punto2=None):
        if punto1 is None:
            punto1 = Punto(0, 0)
        if punto2 is None:
            punto2 = Punto(0, 0)
        self.punto1 = punto1
        self.punto2 = punto2
    
    def base(self):
        return abs(self.punto2.x - self.punto1.x)
    
    def altura(self):
        return abs(self.punto2.y - self.punto1.y)
    
    def area(self):
        return self.base() * self.altura()

# Crear los puntos A(2, 3), B(5, 5), C(-3, -1) y D(0, 0) e imprimirlos por pantalla
A = Punto(2, 3)
B = Punto(5, 5)
C = Punto(-3, -1)
D = Punto(0, 0)
print(A)
print(B)
print(C)
print(D)

# Consultar a qué cuadrante pertenecen los puntos A, C y D
print("El punto A está en el cuadrante", A.cuadrante())
print("El punto C está en el cuadrante", C.cuadrante())
print("El punto D está en el cuadrante", D.cuadrante())

# Consultar los vectores AB y BA
print("El vector AB es", A.vector(B))
print("El vector BA es", B.vector(A))

# (Optativo) Consultar la distancia entre los puntos 'A y B' y 'B y A'
print("La distancia entre los puntos A y B es", A.distancia(B))
print("La distancia entre los puntos B y A es", B.distancia(A))

# (Optativo) Determinar cuál de los puntos A, B o C se encuentra más lejos del origen, punto (0, 0)
dist_A = A.distancia(Punto(0, 0))
dist_B = B.distancia(Punto(0, 0))
dist_C = C.distancia(Punto(0, 0))

if dist_A > dist_B and dist_A > dist_C:
    print("El punto A está más lejos del origen")
elif dist_B > dist_A and dist_B > dist_C:
    print("El punto B está más lejos del origen")
else:
    print("El punto C está más lejos del origen")

# Crear un rectángulo utilizando los puntos A y B
rectangulo_AB = Rectangulo(punto1=A, punto2=B)


base = rectangulo_AB.base()
altura = rectangulo_AB.altura()
area = rectangulo_AB.area()

print("Base: ", base)
print("Altura: ", altura)
print("Área: ", area)
