'''Write a program that acts as a simple calculator. It should take two
numbers and an operator (+, -, *, /) as input and print the result.'''

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y

print("Simple Calculator")
    
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
except ValueError:
    print("Error: Please enter valid numbers.")

operator = input("Enter an operator (+, -, *, /): ")

if operator == '+':
    result = add(num1, num2)
elif operator == '-':
    result = subtract(num1, num2)
elif operator == '*':
    result = multiply(num1, num2)
elif operator == '/':
    result = divide(num1, num2)
else:
    print("Error: Invalid operator.")
   
print(f"The result of {num1} {operator} {num2} is {result}")

