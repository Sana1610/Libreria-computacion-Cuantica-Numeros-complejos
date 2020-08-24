import unittest
import main

class TestMain(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(main.suma([1, 2], [3, 4]), (4, 6))
    def test_resta(self):
        self.assertEqual(main.resta([1, 2], [3, 4]), (-2, -2))
    def test_multiplicar(self):
        self.assertEqual(main.mult([1, 2], [-1, 0]), (-1, -2))
    def test_division(self):
        self.assertEqual(main.divi([1, 2], [3, 4]), (0.44, -0.08))
    def test_sumaVect(self):
        self.assertEqual(main.sumaVec([(1, 2), (3, 4)], [(3, 4), (1, 2)]), [(4, 6), (4,6)])
    def test_inverso(self):
        self.assertEqual(main.inverso([(1, 2), (3, 4)]), [(-1, -2), (-3, -4)])
    def test_escalar_por_vector(self):
        a = [[1,2],[3,4],[5,6]]
        self.assertEqual(main.EscxVect(a, [-1,0]), [(-1,-2),(-3,-4),(-5,-6)])
    def test_suma_matrices(self):
        a = [[[1,2],[3,4],[5,6]],[[10,11],[12,13],[14,15]],[[6,5],[4,3],[2,1]]]
        b = [[[1,2],[3,4],[5,6]],[[10,11],[12,13],[14,15]],[[6,5],[4,3],[2,1]]]
        self.assertEqual(main.Sum_Ma(a,b), [[(2,4),(6,8),(10,12)],[(20,22),(24,26),(28,30)],[(12,10),(8,6),(4,2)]])
    def test_matriz_inversa(self):
        a = [[[1,2],[3,4],[5,6]],[[10,11],[12,13],[14,15]],[[6,5],[4,3],[2,1]]]
        self.assertEqual(main.Inver_Mat(a), [[(-1,-2),(-3,-4),(-5,-6)],[(-10,-11),(-12,-13),(-14,-15)],[(-6,-5),(-4,-3),(-2,-1)]])
    def test_escalar_por_matriz(self):
        a = [[[1,2],[3,4],[5,6]],[[10,11],[12,13],[14,15]],[[6,5],[4,3],[2,1]]]
        self.assertEqual(main.MatxEsc(a,[1,0]), [[(1,2),(3,4),(5,6)],[(10,11),(12,13),(14,15)],[(6,5),(4,3),(2,1)]])
    def test_trasnpuesta(self):
        a = [[(6,10),(2,0),(2,2)],[(0,1),(10,10),(4,5)],[(8,16),(11,10),(21,0)]]
        self.assertEqual(main.Transp(a), [[(6,10),(0,1),(8,16)],[(2,0),(10,10),(11,10)],[(2,2),(4,5),(21,0)]])
    def test_matriz_conjugada(self):
        a = [[[1,2],[3,4],[5,6]],[[10,11],[12,13],[14,15]],[[6,5],[4,3],[2,1]]]
        self.assertEqual(main.conj_ma(a), [[(1,-2),(3,-4),(5,-6)],[(10,-11),(12,-13),(14,-15)],[(6,-5),(4,-3),(2,-1)]])
    def test_matriz_adjunta(self):
        a = [[[6,10],[2,0],[2,2]],[[0,1],[10,10],[4,5]],[[8,16],[11,10],[21,0]]]
        self.assertEqual(main.adjunta(a), [[(6,-10),(0,-1),(8,-16)],[(2,0),(10,-10),(11,-10)],[(2,-2),(4,-5),(21,0)]])
    def test_multiplicacion_matrices(self):
        a = [[[1,0]],[[2,2]]]
        b = [[[3,2],[1,0]]]
        self.assertEqual(main.Mul_Ma(b,a), [[(5, 4),(0, 0)]])
    def test_accion(self):
        a = [[[1,0],[3,1]],[[2,2],[1,1]]]
        b = [[1,0],[0,1]]
        self.assertEqual(main.Accion(a,b), [(0,3),(1,3)])
    def test_producto_interno(self):
        a = [[2,1],[3,2],[1,1]]
        b = [[5,6],[4,8],[16,1]]
        self.assertEqual(main.interno(a,b), (61,8))
    def test_norma(self):
        self.assertEqual(main.norma([[2,1],[3,2],[1,1]]), 4.47)
    def test_distacia(self):
        a = [[2,1],[3,2], [1,1]]
        b = [[5,6],[4,8], [16,1]]
        self.assertEqual(main.distancia(a,b), 17.2)
    def test_unitaria(self):
        a = [[[2,1],[3,2]],[[1,1],[4,1]]]
        self.assertEqual(main.unitaria(a), False)
    def test_hermitiana(self):
        a = [[[1,0],[3,20]],[[3,-20],[5,0]]]
        self.assertEqual(main.hermitiana(a), False)
    def test_tensor(self):
        a = [[[0,0],[1,0]],[[1,0],[0,0]]]
        b = [[[4,0],[2,3],[1,1]],[[1,0],[0,1],[1,0]],[[2,2],[3,3],[4,4]]]
        self.assertEqual(main.tensor(a, b),[[(0,0),(0,0),(0,0),(4,0),(2,3),(1,1)],[(0,0),(0,0),(0,0),(4,0),(2,3),(1,1)]])