import unittest
from conversor_temperatura import (
    celsius_para_fahrenheit,
    fahrenheit_para_celsius,
    celsius_para_kelvin,
    kelvin_para_celsius,
    fahrenheit_para_kelvin,
    kelvin_para_fahrenheit,
    converter_temperatura
)

class TestConversorTemperatura(unittest.TestCase):

    def test_celsius_para_fahrenheit(self):
        self.assertAlmostEqual(celsius_para_fahrenheit(0), 32.0)
        self.assertAlmostEqual(celsius_para_fahrenheit(100), 212.0)

    def test_fahrenheit_para_celsius(self):
        self.assertAlmostEqual(fahrenheit_para_celsius(32), 0.0)
        self.assertAlmostEqual(fahrenheit_para_celsius(212), 100.0)

    def test_celsius_para_kelvin(self):
        self.assertAlmostEqual(celsius_para_kelvin(0), 273.15)
        self.assertAlmostEqual(celsius_para_kelvin(-273.15), 0.0)

    def test_kelvin_para_celsius(self):
        self.assertAlmostEqual(kelvin_para_celsius(273.15), 0.0)

    def test_fahrenheit_para_kelvin(self):
        self.assertAlmostEqual(fahrenheit_para_kelvin(32), 273.15, places=2)

    def test_kelvin_para_fahrenheit(self):
        self.assertAlmostEqual(kelvin_para_fahrenheit(273.15), 32.0, places=2)

    def test_converter_mesma_unidade(self):
        self.assertEqual(converter_temperatura(100, 'C', 'C'), 100)

    def test_converter_combinacoes_validas(self):
        self.assertAlmostEqual(converter_temperatura(100, 'C', 'F'), 212.0)
        self.assertAlmostEqual(converter_temperatura(100, 'C', 'K'), 373.15)
        self.assertAlmostEqual(converter_temperatura(212, 'F', 'C'), 100.0)
        self.assertAlmostEqual(converter_temperatura(212, 'F', 'K'), 373.15, places=2)
        self.assertAlmostEqual(converter_temperatura(0, 'K', 'C'), -273.15)
        self.assertAlmostEqual(converter_temperatura(0, 'K', 'F'), -459.67, places=2)

    def test_converter_invalida(self):
        self.assertIsInstance(converter_temperatura(100, 'X', 'F'), str)
        self.assertIsInstance(converter_temperatura(100, 'C', 'Z'), str)
        self.assertIn("Erro", converter_temperatura(100, 'C', 'Z'))

if __name__ == '__main__':
    unittest.main()
