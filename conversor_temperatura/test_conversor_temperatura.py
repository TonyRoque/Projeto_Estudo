 # test_conversor_temperatura.py

import unittest
from conversor_temperatura import (
    celsius_para_fahrenheit,
    fahrenheit_para_celsius,
    celsius_para_kelvin
)

class TestConversorTemperatura(unittest.TestCase):

    def test_celsius_para_fahrenheit(self):
        self.assertAlmostEqual(celsius_para_fahrenheit(0), 32.0)
        self.assertAlmostEqual(celsius_para_fahrenheit(100), 212.0)
        self.assertAlmostEqual(celsius_para_fahrenheit(-40), -40.0)

    def test_fahrenheit_para_celsius(self):
        self.assertAlmostEqual(fahrenheit_para_celsius(32), 0.0)
        self.assertAlmostEqual(fahrenheit_para_celsius(212), 100.0)
        self.assertAlmostEqual(fahrenheit_para_celsius(-40), -40.0)

    def test_celsius_para_kelvin(self):
        self.assertAlmostEqual(celsius_para_kelvin(0), 273.15)
        self.assertAlmostEqual(celsius_para_kelvin(100), 373.15)
        self.assertAlmostEqual(celsius_para_kelvin(-273.15), 0.0)

if __name__ == "__main__":
    unittest.main()

