# cli.py
# Author: Adugna Gizaw
# Email: gizawadugna@gmail.com
# Phone: +251925582067
# Date: October 29, 2023  (Update with current date)
# Description: This file implements a command-line interface for temperature conversions.

import argparse
from converter import celsius_to_fahrenheit, fahrenheit_to_celsius, celsius_to_kelvin, kelvin_to_celsius, fahrenheit_to_kelvin, kelvin_to_fahrenheit
from logger import log_conversion

def main():
    parser = argparse.ArgumentParser(description="Convert temperatures between Celsius, Fahrenheit, and Kelvin.")
    parser.add_argument("temperature", type=float, help="The temperature value.")
    parser.add_argument("input_unit", choices=["Celsius", "Fahrenheit", "Kelvin"], help="The input temperature unit.")
    parser.add_argument("output_unit", choices=["Celsius", "Fahrenheit", "Kelvin"], help="The output temperature unit.")

    args = parser.parse_args()

    temperature = args.temperature
    input_unit = args.input_unit
    output_unit = args.output_unit

    try:
        if input_unit == output_unit:
            converted_temperature = temperature  # No conversion needed
        elif input_unit == "Celsius":
            if output_unit == "Fahrenheit":
                converted_temperature = celsius_to_fahrenheit(temperature)
            elif output_unit == "Kelvin":
                converted_temperature = celsius_to_kelvin(temperature)
        elif input_unit == "Fahrenheit":
            if output_unit == "Celsius":
                converted_temperature = fahrenheit_to_celsius(temperature)
            elif output_unit == "Kelvin":
                converted_temperature = fahrenheit_to_kelvin(temperature)
        elif input_unit == "Kelvin":
            if output_unit == "Celsius":
                converted_temperature = kelvin_to_celsius(temperature)
            elif output_unit == "Fahrenheit":
                converted_temperature = kelvin_to_fahrenheit(temperature)
        else:
            raise ValueError("Invalid conversion.")

        print(f"{temperature} {input_unit} is {converted_temperature} {output_unit}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e: # Catch any other exceptions
        print(f"An unexpected error occurred: {e}")



if __name__ == "__main__":
    main()