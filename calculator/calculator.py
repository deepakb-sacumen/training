""" Implemented the calculator using switch case """

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiple(a, b):
    return a * b

def devide(a, b):
    return a / b

enterYourFunction = {
    1: add,
    2: subtract,
    3: multiple,
    4: devide
}

def switch(operation, a, b):
  return enterYourFunction.get(operation)(a, b)

print('''enter_your_perform_operation:~
                    1. Addition
                    2. Subtraction
                    3. Multiplication
                    4. Division''')

# To Take input from user
choice = int(input("Select operation from 1,2,3,4 : "))

if choice>=1 and choice<=4:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print (switch(choice, a, b))

else:
    print("Enter valid Your Function between 1 to 4")
