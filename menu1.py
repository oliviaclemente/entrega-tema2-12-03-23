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

# Función para leer un punto desde el teclado
def leer_punto():
    x = int(input("Introduce la coordenada X del punto: "))
    y = int(input("Introduce la coordenada Y del punto: "))
    return Punto(x, y)

# Función para mostrar las opciones del menú
def mostrar_menu():
    print("1. Crear un punto")
    print("2. Calcular el cuadrante de un punto")
    print("3. Calcular el vector entre dos puntos")
    print("4. Calcular la distancia entre dos puntos")
    print("0. Salir")

# Función principal del programa
def main():
    opcion = None
    while opcion != 0:
        mostrar_menu()
        opcion = int(input("Introduce una opción: "))
        if opcion == 1:
            p = leer_punto()
            print("Punto creado:", p)
        elif opcion == 2:
            p = leer_punto()
            print(p.cuadrante())
        elif opcion == 3:
            p1 = leer_punto()
            p2 = leer_punto()
            print(p1.vector(p2))
        elif opcion == 4:
            p1 = leer_punto()
            p2 = leer_punto()
            print(p1.distancia(p2))
        elif opcion == 0:
            print("Hasta luego!")
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()
