FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

try:
    temp = float(input("Enter the temperature to convert: "))
except ValueError:
    print("Invalid temperature. Please enter a numeric value.")
else:
    units = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if units == "C":
        conv_temp = convert_to_fahrenheit(temp)
        print(f"{temp}\u00B0C is {conv_temp}\u00B0F")
    elif units == "F":
        conv_temp = convert_to_celsius(temp)
        print(f"{temp}\u00B0F is {conv_temp}\u00B0C")
    else:
        print("Invalid Unit of Measure")
