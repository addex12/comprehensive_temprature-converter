# logger.py
# Author: Adugna Gizaw
# Email: gizawadugna@gmail.com
# Phone: +251925582067
# Date: October 27, 2023 (or update with current date)
# Description: This file contains functions for logging temperature conversions.

import logging

# Configure logging
logging.basicConfig(filename='temperature_conversion.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def log_conversion(input_temp, input_unit, output_temp, output_unit):
    """Logs a temperature conversion."""
    message = f"Converted {input_temp} {input_unit} to {output_temp} {output_unit}"
    logging.info(message)


# Example Usage (this will only run when you execute logger.py directly)
if __name__ == "__main__":
    log_conversion(0, "Celsius", 32, "Fahrenheit")
    log_conversion(100, "Celsius", 212, "Fahrenheit")
    log_conversion(32, "Fahrenheit", 0, "Celsius")
    log_conversion(273.15, "Kelvin", 0, "Celsius")
    log_conversion(68, "Fahrenheit", 293.15, "Kelvin")
    log_conversion(298.15, "Kelvin", 77, "Fahrenheit")