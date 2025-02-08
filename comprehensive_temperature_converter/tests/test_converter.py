# tests/test_converter.py
# Author: Adugna Gizaw
# Email: gizawadugna@gmail.com
# Phone: +251925582067
# Date: October 30, 2023 (Update with current date)
# Description: Unit tests for the temperature conversion functions in converter.py

import unittest
from converter import celsius_to_fahrenheit, fahrenheit_to_celsius, celsius_to_kelvin, kelvin_to_celsius, fahrenheit_to_kelvin, kelvin_to_fahrenheit

class TestConverter(unittest.TestCase):

    def test_celsius_to_fahrenheit(self):
        self.assertEqual(celsius_to_fahrenheit(0), 32)
        self.assertEqual(celsius_to_fahrenheit(100), 212)
        self.assertEqual(celsius_to_fahrenheit(-40), -40)  # Edge case
        self.assertAlmostEqual(celsius_to_fahrenheit(25), 77) # Use assertAlmostEqual for floating-point comparisons

    def test_fahrenheit_to_celsius(self):
        self.assertEqual(fahrenheit_to_celsius(32), 0)
        self.assertEqual(fahrenheit_to_celsius(212), 100)
        self.assertEqual(fahrenheit_to_celsius(-40), -40)  # Edge case
        self.assertAlmostEqual(fahrenheit_to_celsius(77), 25)

    def test_celsius_to_kelvin(self):
        self.assertAlmostEqual(celsius_to_kelvin(0), 273.15)
        self.assertAlmostEqual(celsius_to_kelvin(100), 373.15)
        self.assertAlmostEqual(celsius_to_kelvin(-273.15), 0)  # Absolute zero
        self.assertAlmostEqual(celsius_to_kelvin(25), 298.15)

    def test_kelvin_to_celsius(self):
        self.assertAlmostEqual(kelvin_to_celsius(273.15), 0)
        self.assertAlmostEqual(kelvin_to_celsius(373.15), 100)
        self.assertAlmostEqual(kelvin_to_celsius(0), -273.15)  # Absolute zero
        self.assertAlmostEqual(kelvin_to_celsius(298.15), 25)

    def test_fahrenheit_to_kelvin(self):
        self.assertAlmostEqual(fahrenheit_to_kelvin(32), 273.15)
        self.assertAlmostEqual(fahrenheit_to_kelvin(212), 373.15)
        self.assertAlmostEqual(fahrenheit_to_kelvin(-459.67), 0)  # Absolute zero
        self.assertAlmostEqual(fahrenheit_to_kelvin(68), 293.15)

    def test_kelvin_to_fahrenheit(self):
        self.assertAlmostEqual(kelvin_to_fahrenheit(273.15), 32)
        self.assertAlmostEqual(kelvin_to_fahrenheit(373.15), 212)
        self.assertAlmostEqual(kelvin_to_fahrenheit(0), -459.67)  # Absolute zero
        self.assertAlmostEqual(kelvin_to_fahrenheit(293.15), 68)


if __name__ == '__main__':
    unittest.main()