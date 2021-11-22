def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("Calculator\n 1. Add\n 2. Subtract\n 3. Multiply\n 4. Divide")

while True:
    choice = int(input("Please enter your choice(1/2/3/4): "))

    if choice in [1,2,3,4]:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        
        ops = {
        1: add,
        2: subtract,
        3: multiply,
        4: divide,
        }
        
        chosen_op = ops.get(choice)
        answer = chosen_op(num1, num2)
        print(answer)
        
        continue_op = input("Do you want to continue? (y/n): ")
        if continue_op == "n":
          break
          
    else:
        print("Please enter a valid input")
