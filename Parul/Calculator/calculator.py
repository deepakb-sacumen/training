def addition(num1, num2):
  return num1 + num2

def subtraction(num1, num2):
  return num1 - num2

def multiply(num1, num2):
  return num1 * num2

def division(num1, num2):
  try:
    return num1/num2
  except ZeroDivisionError:
      print('Cannot divide by zero')
  
def default(num1, num2):
  return "Incorrect operarion"

def calculate(operation, num1, num2):
    operations = {
    'add': addition,
    'substract': subtraction,
    'multiply': multiply,
    'divide': division
    }

    return operations.get(operation, default)(num1, num2)

print('''Select operation to perform:
1. add
2. substract
3. multiply
4. divide ''')

try:
  # Take input from user
  choice = input("Enter the operation: ")
  num1 = int(input("Enter first number: "))
  num2 = int(input("Enter second number: "))
  print ("Result: ", calculate(choice, num1, num2))
except ValueError:
  print("Incorrect value")