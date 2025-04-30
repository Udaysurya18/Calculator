def calculator():
    print("Simple Calculator - Only Addition and Subtraction")
    num1 = float(input("Enter the first number: "))
    operation = input("Enter '+' for addition or '-' for subtraction: ")
    num2 = float(input("Enter the second number: "))

    if operation == '+':
        result = num1 + num2
        print(f"Result: {num1} + {num2} = {result}")
    elif operation == '-':
        result = num1 - num2
        print(f"Result: {num1} - {num2} = {result}")
    else:
        print("Invalid operation. Please use '+' or '-'.")

calculator()