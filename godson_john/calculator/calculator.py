def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        result = 0
    return result

def calculate(choice, num1, num2):
        ops = {
        '1': add,
        '2': subtract,
        '3': multiply,
        '4': divide,
        }
        chosen_op = ops.get(choice)
        result = chosen_op(num1, num2)
        return result

continue_op = True
while continue_op:
    print("Calculator\n 1. Add\n 2. Subtract\n 3. Multiply\n 4. Divide\n")
    choice = input("Please enter your choice(1/2/3/4): ")
    if choice in ['1','2','3','4']:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        result = calculate(choice, num1, num2)
        print("The answer is: ", result)
    else:
        print("Invalid input")
        
    continue_op = input("\nDo you want to continue? (y/n): ")
    if continue_op.lower() == "n":
        continue_op = False
    