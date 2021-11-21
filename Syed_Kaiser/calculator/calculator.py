
import pdb
from constants import INCORRECT_VALUES
from messages import INVALID_INPUT, TYPE_ERROR, USER_INPUT_MSSG

try:
    class testCalculator():

        def __init__(self,x,y):
            self.x = x
            self.y = y

        
        def add(x,y):
            return (x+y)

        def sub(x,y):
            return (x-y)

        def mul(x,y):
            return (x*y)
            
        def div(x,y):
            return (x/y)

        def default():
            return INCORRECT_VALUES

        calculator = {

            "1": add,
            "2": sub,
            "3": mul,
            "4": div

        }

        def switch(self,operation):
            return self.calculator.get(operation, self.default)(x,y)

    # x,y = input("enter the values separated by a space: ").split()
    x, y = 10,0

    operation = str(input(USER_INPUT_MSSG))

    if operation:
        operate = testCalculator(int(x),int(y))
        res = operate.switch(operation)

        print(res)

except NameError as e:
    print(INVALID_INPUT)

except TypeError as e:
    print(TYPE_ERROR.format(operation))

except SyntaxError as e:
    print("{}: {}".format(type(e).__name__,e))

except ZeroDivisionError as e:
    print("{}: {}".format(type(e).__name__,e))