import argparse
import tkinter as tk
from tkinter import ttk, messagebox
from rich import print
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt
from converter import celsius_to_fahrenheit, fahrenheit_to_celsius, celsius_to_kelvin, kelvin_to_celsius, fahrenheit_to_kelvin, kelvin_to_fahrenheit
from logger import log_conversion

console = Console()

def get_temperature_input():
    while True:
        try:
            temperature = float(Prompt.ask("[bold blue]Enter the temperature value[/bold blue]"))
            return temperature
        except ValueError:
            console.print("[bold red]Invalid input. Please enter a number.[/bold red]")

def get_unit_input(prompt_message):
    while True:
        unit = Prompt.ask(prompt_message).lower()
        if unit in ["celsius", "fahrenheit", "kelvin"]:
            return unit.capitalize()
        else:
            console.print("[bold red]Invalid unit. Please enter Celsius, Fahrenheit, or Kelvin.[/bold red]")

def show_popup(input_temp, input_unit, output_temp, output_unit, temp_input, unit_input, unit_output):
    popup = tk.Tk()
    popup.withdraw()

    message = f"Temperature Input: {temp_input}\nUnit Input: {unit_input}\nUnit Output: {unit_output}\n\nResult: {input_temp} {input_unit} = {output_temp} {output_unit}"  # More detailed message
    messagebox.showinfo("Conversion Result", message)


def main():
    temperature = get_temperature_input()
    input_unit = get_unit_input("[bold green]What is the input unit?[/bold green] (Celsius, Fahrenheit, Kelvin)")
    output_unit = get_unit_input("[bold yellow]What unit do you want to convert to?[/bold yellow] (Celsius, Fahrenheit, Kelvin)")

    try:
        if input_unit == output_unit:
            converted_temperature = temperature
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

        # Show popup with all inputs
        show_popup(temperature, input_unit, converted_temperature, output_unit, temperature, input_unit, output_unit)  # Pass all input values

        # Rich output (still keep it for console logging/feedback)
        panel_title = f"[bold blue]Temperature Conversion Result[/bold blue]"
        table = Table(title=panel_title, style="cyan")
        table.add_column("Input", style="magenta")
        table.add_column("Output", style="green")
        table.add_row(f"{temperature} {input_unit}", f"{converted_temperature} {output_unit}")
        console.print(Panel(table, border_style="yellow"))

        log_conversion(temperature, input_unit, converted_temperature, output_unit)

    except ValueError as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
    except Exception as e:
        console.print(f"[bold red]An unexpected error occurred:[/bold red] {e}")

if __name__ == "__main__":
    main()