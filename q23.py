'''Write a program that converts temperature from Celsius to Fahrenheit
and vice versa based on user input.'''

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9


print("Temperature Converter")
print("Select the conversion:")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
    
choice = input("Enter 1 or 2: ")

if choice == '1':
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")
elif choice == '2':
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")
else:
    print("Invalid choice. Please select 1 or 2.")


