import unittest
import main

class TestMain(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(main.suma([1, 2, 3, 4]), [4, 6])
    def test_resta(self):
        self.assertEqual(main.resta([1, 2, 3, 4]), [-2, -2])
    def test_multiplicar(self):
        self.assertEqual(main.mult([1, 2, 3, 4]), [-5, 10])
    def test_division(self):
        self.assertEqual(main.divi([1, 2, 3, 4]), [0.44, -0.08])
    def test_modulo(self):
        self.assertEqual(main.modu([3, 4]), 5.0)
    def test_conjugado(self):
        self.assertEqual(main.conj([3, 4]), [3, -4])
    def test_fase(self):
        self.assertEqual(main.fase([3, 4]), 0.93)
    def test_cartpol(self):
        self.assertEqual(main.car_pol([3, 4]), [5.0, 0.93])
    def test_polcart(self):
        self.assertEqual(main.pola([2.24, 1.11]), [0.89, 1.79])