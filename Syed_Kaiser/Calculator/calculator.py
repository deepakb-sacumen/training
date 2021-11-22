class Test_calculator:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    
    def add(self):
        return (self.x+self.y)

    def sub(self):
        return (self.x-self.y)

    def mul(self):
        return (self.x*self.y)
        
    def div(self):
        return (self.x/self.y)

    def switch(self,operation):

        calculator = {

            "1": self.add,
            "2": self.sub,
            "3": self.mul,
            "4": self.div
        }
        return calculator.get(operation)()

if __name__ == "__main__":
    
    try:
        x = int(input("enter first value: "))
        y = int(input("enter second value: "))
        operation = str(input('Select any of the following operations: [1. Addition, 2. Subtraction, 3. Multiplication, 4. Division]: '))

        if operation and type(x) == type(y) == int:
            operate = Test_calculator(x,y)
            res = operate.switch(operation)
            print(res)

        elif not operation or operation == '' and not x or not y:
            print("Incorrect input")


    except ZeroDivisionError as e:
        print("{}: {}".format(type(e).__name__,e))
        
    except NameError as e:
        print("INVALID_INPUT")

    except TypeError as e:
        print("TYPE ERROR")

    except SyntaxError as e:
        print("{}: {}".format(type(e).__name__,e))

    except ValueError as e:
        print("{}: {}".format(type(e).__name__,e))