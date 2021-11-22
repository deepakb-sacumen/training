"""Calculator used for calculating add, sub, mul, div, mod"""

def addition(num1, num2):
  """Addition of two numbers"""
  num1 += num2
  return num1

def subtraction(num1, num2):
  """Substraction of two numbers"""
  num1 -= num2
  return num1

def mul(num1, num2):
  """Multiplication of two numbers"""
  num1 *= num2
  return num1

def division(num1, num2):
  """Division of two numbers"""
  try:
    num1 /= num2
    return num1
  except ZeroDivisionError:
    return "Invalid arithematic operation"
  
def module(num1, num2):
  """Modules of two numbers."""
  num1 %= num2
  return num1

def default(num1, num2):
  return "Incorrect operation"

operator = {
    "add": addition,
    "sub": subtraction,
    "mul": mul,
    "div": division,
    "mod": module
}
def executor(operation, num1, num2):
  """Execute particular operation."""
  return operator.get(operation, default)(num1, num2)

print('''Perform any below operation:
add. Addition
sub. Subtraction
mul. Multiplication
div. Division
mod. Module ''')
# Take input from user
try:
  choice = input("Select operation from add,sub,mul,div,mod : ")
  num1 = int(input("Enter first number: "))
  num2 = int(input("Enter second number: "))
  print (executor(choice, num1, num2))
except ValueError:
  print("Invalid argument passed")
