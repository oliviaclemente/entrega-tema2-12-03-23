import math
from punto import Punto

def test_crear_punto():
    print("Comprobando la creación de un punto...")
    punto = Punto()
    assert punto.x == 0
    assert punto.y == 0
    
    punto = Punto(3, 4)
    assert punto.x == 3
    assert punto.y == 4
    
def test_str():
    print("Comprobando la representación de un punto...")
    punto = Punto(3, 4)
    assert str(punto) == "(3,4)"
    
def test_cuadrante():
    print("Comprobando el cuadrante de un punto...")
    punto = Punto(3, 4)
    assert punto.cuadrante() == "El punto (3,4) pertenece al primer cuadrante"
    
    punto = Punto(-3, 4)
    assert punto.cuadrante() == "El punto (-3,4) pertenece al segundo cuadrante"
    
    punto = Punto(-3, -4)
    assert punto.cuadrante() == "El punto (-3,-4) pertenece al tercer cuadrante"
    
    punto = Punto(3, -4)
    assert punto.cuadrante() == "El punto (3,-4) pertenece al cuarto cuadrante"
    
    punto = Punto(0, 4)
    assert punto.cuadrante() == "El punto (0,4) se sitúa sobre el eje Y"
    
    punto = Punto(3, 0)
    assert punto.cuadrante() == "El punto (3,0) se sitúa sobre el eje X"
    
    punto = Punto(0, 0)
    assert punto.cuadrante() == "El punto (0,0) está sobre el origen"
    
def test_vector():
    print("Comprobando el vector entre dos puntos...")
    punto1 = Punto(3, 4)
    punto2 = Punto(-1, 2)
    assert punto1.vector(punto2) == "El vector resultante entre (3,4) y (-1,2) es (-4,-2)"
    
def test_distancia():
    print("Comprobando la distancia entre dos puntos...")
    punto1 = Punto(3, 4)
    punto2 = Punto(-1, 2)
    assert math.isclose(punto1.distancia(punto2), 5.0, rel_tol=1e-9)

if __name__ == "__main__":
    test_crear_punto()
    test_str()
    test_cuadrante()
    test_vector()
    test_distancia()
    print("Todos los tests han pasado")
