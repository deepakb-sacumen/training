# a = int(input("Enter a value"))
# b = int(input("Enter b value"))
# c = a+b

def add(a, b):
    a += b
    return a

def subtract(a, b):
    a -= b
    return a

def multiple(a, b):
    a *= b
    return a

def devide(a, b):
    a /= b
    return a

enter_your_function = {
    1: add,
    2: subtract,
    3: multiple,
    4: devide
}
def switch(operation, a, b):
  return enter_your_function.get(operation)(a, b)
print('''enter_your_perform_operation:~
                    1. Addition
                    2. Subtraction
                    3. Multiplication
                    4. Division''')
# To Take input from user
choice = int(input("Select operation from 1,2,3,4 : "))
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print (switch(choice, a, b))