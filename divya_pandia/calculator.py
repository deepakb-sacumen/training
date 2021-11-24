"""Implementation of Calculator using switch case in Python"""

def addition(a,b):
        return a+b

def subtraction(a,b):
        return a-b

def multiplication(a,b):
        return a*b

def division(a,b):
        return a/b

def modulus(a,b):
        return a%b

def default():
        return "No inputs"

switcher = {
    0: addition(5,4),
    1: subtraction(5,4),
    2: multiplication(5,4),
    3: division(5,4),
    4: modulus(5,4)
}

def calculate(operation):
    return switcher.get(operation,default)

print(calculate(2))



