celsius_unit = 0
fahrenheit_unit = 0
kelvin_unit = 0

celsius_unit = float(input("Ingrese la temperatura en Celsius: "))
fahrenheit_unit = (celsius_unit * 9/5) + 32
kelvin_unit = celsius_unit + 273.15

print (f"fahrenheit: {fahrenheit_unit}°F")
print (f"kelvin: {kelvin_unit}°K")