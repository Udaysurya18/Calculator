def calculator():
    print("Simple Calculator - Addition, Subtraction, and Multiplication")
    num1 = float(input("Enter the first number: "))
    operation = input("Enter '+', '-', or '*' for the operation: ")
    num2 = float(input("Enter the second number: "))

    if operation == '+':
        result = num1 + num2
        print(f"Result: {num1} + {num2} = {result}")
    elif operation == '-':
        result = num1 - num2
        print(f"Result: {num1} - {num2} = {result}")
    elif operation == '*':
        result = num1 * num2
        print(f"Result: {num1} * {num2} = {result}")
    else:
        print("Invalid operation. Please use '+', '-', or '*'.")

calculator()
