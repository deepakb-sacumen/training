# a = int(input("Enter a value"))
# b = int(input("Enter b value"))
# c = a+b
class Calculator:
    def add(self,a,b):
        c = a+b
        return c
    def subtract(self,a,b):
        c = a-b
        return c
    def multiple(self,a,b):
        c = a*b
        return c
    def devide(self,a,b):
        c = a/b
        return c

print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
  print("Please_enter_your_function (1-4): ")

  try:
     cals_obj = Calculator()
     enter_your_function = int(input())

     if enter_your_function>=1 and enter_your_function<=4:
        a = float(input("Enter a Value :~ "))
        b = float(input("Enter b Value :~ "))

        if enter_your_function == 1:
            print(cals_obj.add(a, b))

        elif enter_your_function == 2:
            print( str(cals_obj.subtract(a, b)))

        elif enter_your_function == 3:
            print( str(cals_obj.multiple(a, b)))

        elif enter_your_function == 4:
            print(str(cals_obj.devide(a, b)))
            break
     else:
        print("Invalid Entry..Please_enter_your_function")


  except ValueError:
     print("Invalid Entry..Please_enter_your_function")
     continue
