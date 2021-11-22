

from typing import Any


class calc():
    def __init__(self,num1,num2) -> None:
        self.num1=num1
        self.num2 = num2
        
    def add(self) -> int:
        return self.num1+self.num2

    def subtract(self) -> int:
        return self.num1-self.num2

    def multiply(self) -> Any:
        return self.num1*self.num2     

    def divide(self) -> Any:
        return self.num1/self.num2

if __name__ == "__main__":

    print('''You can perform operation
    1. Addition as add
    2. Subtraction as sub
    3. Multiplication as multiply
    4. Division as divide
    ''')


    def calculate(operation_key, num1, num2):
        calculator = calc(num1,num2)
        operations = {
        'add': calculator.add(),
        'sub' : calculator.subtract(),
        'multiply' : calculator.multiply(),
        'divide': calculator.divide(),
        }
        return operations.get(operation_key)

    try :
        operation_key = input("Enter the operation of two integer numbers:")
        num1 = int(input("Enter first number : "))
        num2 = int(input("Enter second number : "))
        res = calculate(operation_key, num1, num2)

    except ValueError:
        print("Entered Unsupported values")

    else:
        result = print(f"Result is {res}")

    