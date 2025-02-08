```markdown
# README.md

# Temperature Converter

This Python package provides functions for converting temperatures between Celsius, Fahrenheit, and Kelvin. It also includes a command-line interface (CLI) for easy conversions and logging functionality to track conversions.

## Installation

This section guides you through setting up the Temperature Converter package.

1. **Clone the repository:**

   Open your terminal or command prompt and navigate to the directory where you want to store the project. Then, clone the repository using Git:

   ```bash
   git clone [https://github.com/addex12/comprehensive_temperature_converter.git](https://github.com/addex12/temperature_converter.git)
   ```

   This command will create a directory named `comprehensive_temperature_converter` containing the project files.

2. **Navigate to the project directory:**

   ```bash
   cd comprehensive_temperature_converter
   ```

3. **(Optional but Highly Recommended) Create and activate a virtual environment:**

   Using a virtual environment isolates your project's dependencies from your system's Python installation and prevents conflicts.

   * **Create a virtual environment:**

     ```bash
     python3 -m venv .venv  # Creates a virtual environment named ".venv"
     ```

   * **Activate the virtual environment:**

     * **Linux/macOS:**
       ```bash
       source .venv/bin/activate
       ```
     * **Windows:**
       ```bash
       .venv\Scripts\activate
       ```

     You should see the name of the virtual environment (e.g., `.venv`) in parentheses in your terminal prompt, indicating that it's active.

4. **(Optional) Install dependencies:**

   Although this project currently has no external dependencies, it's good practice to include this step. If any dependencies were listed in a `requirements.txt` file, you would install them using pip:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

This section explains how to use the Temperature Converter, both from the command line and as a Python library.

### Command-Line Interface (CLI)

The `cli.py` script provides a convenient way to perform conversions from the command line.

1. **Run the `cli.py` script:**

   Use the following command structure:

   ```bash
   python cli.py <temperature> <input_unit> <output_unit>
   ```

   * `<temperature>`: The numerical value of the temperature.
   * `<input_unit>`: The unit of the input temperature (Celsius, Fahrenheit, or Kelvin).
   * `<output_unit>`: The desired unit for the converted temperature (Celsius, Fahrenheit, or Kelvin).

2. **Examples:**

   * **Convert 25 Celsius to Fahrenheit:**
     ```bash
     python cli.py 25 Celsius Fahrenheit
     ```

   * **Convert 98.6 Fahrenheit to Kelvin:**
     ```bash
     python cli.py 98.6 Fahrenheit Kelvin
     ```

   * **Convert 273.15 Kelvin to Celsius:**
     ```bash
     python cli.py 273.15 Kelvin Celsius
     ```

   * **No conversion (same units):**
     ```bash
     python cli.py 25 Celsius Celsius
     ```

3. **Handling invalid input:**

   The CLI is designed to handle some invalid input, but it's important to be aware of how to use it correctly.

   * **Incorrect units:** If you provide incorrect unit names (e.g., "celsius" instead of "Celsius"), the CLI will display an error message with the available unit options and exit.
   * **Non-numerical temperature:** If you enter a non-numerical value for the temperature, the CLI will display an error message.
   * **Missing arguments:** If you don't provide all three arguments (temperature, input unit, and output unit), the CLI will display a help message showing the correct usage.

4. **Output and Logging:**

   The CLI will print the converted temperature to the console.  All conversions, including the input and output values and units, are also logged to the `temperature_conversion.log` file in the same directory.

### Python Library

You can also use the conversion functions directly within your Python scripts.

1. **Import the functions:**

   ```python
   from converter import celsius_to_fahrenheit, fahrenheit_to_celsius, celsius_to_kelvin, kelvin_to_celsius, fahrenheit_to_kelvin, kelvin_to_fahrenheit
   ```

2. **Use the functions:**

   ```python
   temp_f = celsius_to_fahrenheit(25)  # Convert 25 Celsius to Fahrenheit
   print(temp_f)  # Output: 77.0

   temp_c = fahrenheit_to_celsius(98.6)  # Convert 98.6 Fahrenheit to Celsius
   print(temp_c)  # Output: 37.0

   # ... use other conversion functions as needed ...
   ```

   Each conversion function takes the temperature value as an argument and returns the converted temperature.

3. **Logging:**

   Just like with the CLI, all conversions made using the Python library functions are automatically logged to the `temperature_conversion.log` file.

## Running Tests

The unit tests for the conversion functions are located in the `tests` directory, specifically in the `test_converter.py` file.

1. **Navigate to the project's root directory:**

   Make sure you are at the top level of the `temperature_converter` directory in your terminal.

2. **Run the tests:**

   ```bash
   python -m unittest tests/test_converter.py
   ```

   This command will discover and run all the tests defined in `test_converter.py`.  The output will show you whether the tests passed or failed.

## Logging

All temperature conversions, whether performed through the CLI or the Python library, are logged to the `temperature_conversion.log` file. This file is located in the same directory as the `converter.py`, `cli.py`, and `logger.py` files.  You can open this file to review the history of conversions.

## Project Structure

```
comprehensive_temperature_converter/
├── converter.py      # Temperature conversion functions
├── logger.py         # Logging functionality
├── cli.py            # Command-line interface
├── tests/
│   └── test_converter.py  # Unit tests
├── requirements.txt  # Dependencies (empty in this case)
└── README.md         # Documentation
```
