#function definitions for mathematical operations
def addition(num1, num2):
  return num1 + num2

def subtraction(num1, num2):
  if num1 > num2:
    return num1 - num2
  else:
      return num2 - num1  

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num1 > num2:
        return num1/num2
    else:
        return num2/num1

#function mapping to dictionary to replicate switch case funtionality
mathOps = {
    'add': addition,
    'sub': subtraction,
    'mul': multiplication,
    'div': division
}

#function to determine result based on user's input
def switch(operation, num1, num2):
  return mathOps.get(operation,'you chose the wrong operation')(num1, num2)
print('''You can perform operation
1. add
2. sub
3. mul
4. div ''')


#driver code
if __name__ == '__main__':
    mathOpsChoice = input("Select operation: ")
    num1,num2 = input("Enter two numbers: ").split()
    print (switch(mathOpsChoice, int(num1), int(num2)))