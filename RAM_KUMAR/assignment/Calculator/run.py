from calculator import Calculator


if __name__ == "__main__":
    calculator = Calculator()
    operations = {
        'add',
        'subtract',
        'multiply',
        'divide'
    }

    print("Select operation.")
    print("1.add")
    print("2.subtract")
    print("3.multiply")
    print("4.divide")

    while True:
        choice = input("Enter your choice: ")    
        
        if choice in ('add', 'subtract', 'multiply', 'divide'):
            func = getattr(calculator, choice)
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))            
            result = func(num1, num2)
            print ("Your result is...",result)
        else:
            print ("Please select operation from the listed choices")




            