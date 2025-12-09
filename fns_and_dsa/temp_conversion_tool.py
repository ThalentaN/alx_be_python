# fns_and_dsa/temp_conversion_tool.py

# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius using the global conversion factor.
    """
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit using the global conversion factor.
    """
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        temp_input = input("Enter the temperature to convert: ").strip()
        # Check if input is numeric
        if not temp_input.replace('.', '', 1).isdigit() and not (temp_input.startswith('-') and temp_input[1:].replace('.', '', 1).isdigit()):
            raise ValueError
        temp_input = float(temp_input)
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == "F":
            converted = convert_to_celsius(temp_input)
            print(f"{temp_input}°F is {converted}°C")
        elif unit == "C":
            converted = convert_to_fahrenheit(temp_input)
            print(f"{temp_input}°C is {converted}°F")
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()
