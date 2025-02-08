# converter.py
# Author: Adugna Gizaw
# Email: gizawadugna@gmail.com
# Phone: +251925582067
# Date: October 27, 2023 (or update with current date)
# Description: This file contains functions for converting temperatures between Celsius, Fahrenheit, and Kelvin.

from logger import log_conversion  # Import the logging function

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    log_conversion(celsius, "Celsius", fahrenheit, "Fahrenheit")  # Log the conversion
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    log_conversion(fahrenheit, "Fahrenheit", celsius, "Celsius")
    return celsius

def celsius_to_kelvin(celsius):
    kelvin = celsius + 273.15
    log_conversion(celsius, "Celsius", kelvin, "Kelvin")
    return kelvin

def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    log_conversion(kelvin, "Kelvin", celsius, "Celsius")
    return celsius

def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    kelvin = celsius_to_kelvin(celsius)
    log_conversion(fahrenheit, "Fahrenheit", kelvin, "Kelvin")
    return kelvin

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    fahrenheit = celsius_to_fahrenheit(celsius)
    log_conversion(kelvin, "Kelvin", fahrenheit, "Fahrenheit")
    return fahrenheit


# Example usage (optional - can be removed or placed in a separate test file)
if __name__ == "__main__":
    print(f"0 Celsius is {celsius_to_fahrenheit(0)} Fahrenheit")
    print(f"32 Fahrenheit is {fahrenheit_to_celsius(32)} Celsius")
    print(f"25 Celsius is {celsius_to_kelvin(25)} Kelvin")
    print(f"273.15 Kelvin is {kelvin_to_celsius(273.15)} Celsius")
    print(f"68 Fahrenheit is {fahrenheit_to_kelvin(68)} Kelvin")
    print(f"298.15 Kelvin is {kelvin_to_fahrenheit(298.15)} Fahrenheit")