import unittest
import DinamicaDeterminista

class TestMain(unittest.TestCase):
    def test_DinamicaDeterminista(self):
        click = 1
        matriz = [[(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],[(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],[(0,0),(1,0),(0,0),(0,0),(0,0),(1,0)],[(0,0),(0,0),(0,0),(1,0),(0,0),(0,0)],[(0,0),(0,0),(1,0),(0,0),(0,0),(0,0)],[(1,0),(0,0),(0,0),(0,0),(1,0),(0,0)]]
        vectoIni = [(6,0),(2,0),(1,0),(5,0),(3,0),(10,0)]
        self.assertEqual(DinamicaDeterminista.DinamicaDeterminista(click,matriz,vectoIni),[(0, 0), (0, 0), (12, 0), (5, 0), (1, 0), (9, 0)])

    def test_DidanimaDeterProbabilidades(self):
        rendijas = 2
        objetivos = 3
        probabilidades = [(1/3,0),(1/3,0),(1/3,0),(1/3,0),(1/3,0),(1/3,0)]
        self.assertEqual(DinamicaDeterminista.DinamicaDeterministaProbabilidad(rendijas,objetivos,probabilidades),[(0.0, 0.0), (0.0, 0.0), (0.0, 0.0), (1/6, 0.0), (1/6, 0.0), (1/3, 0.0), (1/6, 0.0), (1/6, 0.0)])

DinamicaDeterminista.dibujo([(0.0, 0.0), (0.0, 0.0), (0.0, 0.0), (1/6, 0.0), (1/6, 0.0), (1/3, 0.0), (1/6, 0.0), (1/6, 0.0)])
