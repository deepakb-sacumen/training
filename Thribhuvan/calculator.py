def addition(num1, num2):
    num1 += num2
    return num1


def subtraction(num1, num2):
    num1 -= num2
    return num1


def mul(num1, num2):
    num1 *= num2
    return num1


def division(num1, num2):
    num1 /= num2
    return num1

def default(num1, num2):
  return "Incorrect operation"


switcher = {
    1: addition,
    2: subtraction,
    3: mul,
    4: division
}


def switch(operation, num1, num2):
    return switcher.get(operation, default)(num1, num2)


print('''You can perform operation
1. Addition
2. Subtraction
3. Multiplication
4. Division
''')

choice = int(input("Select operation from 1,2,3,4 : "))
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print(switch(choice, num1, num2))