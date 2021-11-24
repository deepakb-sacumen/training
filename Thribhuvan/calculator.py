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


cal_operations = {
    1: addition,
    2: subtraction,
    3: mul,
    4: division
}


def calculator(operation, num1, num2):
    return cal_operations.get(operation, default)(num1, num2)


print('''You can perform operation
1. Addition
2. Subtraction
3. Multiplication
4. Division
''')

if __name__ == "__main__":
    choice = int(input("Select operation from 1,2,3,4 : "))
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(calculator(choice, num1, num2))
