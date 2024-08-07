# -*- coding: utf-8 -*-
"""8_Operator

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1VOYTKjd1K7D-7QCtUfUqhxCVcbvltBfq
"""

def perform_operation():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operator = input("Enter the operator (+, -, *, /): ")

    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            raise ValueError("Division by zero is not allowed")
    else:
        raise ValueError("Invalid operator. Please use '+', '-', '*', or '/'")

# Example usage:
try:
    result = perform_operation()
    print("Result:", result)
except ValueError as e:
    print(e)

