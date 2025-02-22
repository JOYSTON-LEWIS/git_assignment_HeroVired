# Version 1 Release

# Importing Library for arithmetic operations in python
import math

# Defining Calculator Plus Application Class with its Functions
class Calculator:
    # Addition Function
    def add(self, a, b):
        # Returns Sum of Two Numbers
        return a + b
    
    # Subtraction Function
    def subtract(self, a, b):
        # Returns Difference of Two Numbers
        return a - b
    
    # Multiplication Function
    def multiply(self, a, b):
        # Returns Multiplication of Two Numbers
        return a * b
    
    # Division Function
    def divide(self, a, b):
        # Bug Fix to Handle Division by Zero
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        # Returns Division of Two Numbers
        return a / b

# Main Script Declaration    
if __name__ == "__main__":
    # Creating an instance of the Calculator class
    calculator = Calculator()

    # Defining First Number
    num1 = 16
    
    # Defining Second Number
    num2 = 4
    
    # Printing Addition of Two Numbers
    print(f"{num1} + {num2} = {calculator.add(num1, num2)}")
    
    # Printing Subtraction of Two Numbers
    print(f"{num1} - {num2} = {calculator.subtract(num1, num2)}") 
    
    # Printing Multiplication of Two Numbers
    print(f"{num1} * {num2} = {calculator.multiply(num1, num2)}")
    
    # Printing Division of Two Numbers
    print(f"{num1} / {num2} = {calculator.divide(num1, num2)}")