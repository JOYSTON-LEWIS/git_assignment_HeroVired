# Square Root Feature 

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
    
    # Square Root Function
    def square_root(self, x):
        # Returns Square Root Value of  the Number
        return math.sqrt(x)

# Main Script Declaration    
if __name__ == "__main__":
    # Creating an instance of the Calculator class
    calculator = Calculator()

    # Defining First Number
    num1 = 16
    
    # Defining Second Number
    num2 = 4

    # Defining the Third Number
    num3 = 25
    
    # Printing Addition of Two Numbers
    print(f"{num1} + {num2} = {calculator.add(num1, num2)}")
    
    # Printing Subtraction of Two Numbers
    print(f"{num1} - {num2} = {calculator.subtract(num1, num2)}") 
    
    # Printing Multiplication of Two Numbers
    print(f"{num1} * {num2} = {calculator.multiply(num1, num2)}")
    
    # Printing Division of Two Numbers
    print(f"{num1} / {num2} = {calculator.divide(num1, num2)}")

    # Printing Square Root of the Number
    print(f"The square root of {num3} = {calculator.square_root(num3)}")

