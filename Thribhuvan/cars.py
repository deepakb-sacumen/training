class Vehicle(object):
    def __init__(self, fname):
        self.name = fname
        self.color = "red"
    
    def horn(self):
        print("peep peep")

class Car(Vehicle):
    def __init__(self, fname, num_wheels):
        self.num_wheels = num_wheels
        super().__init__(fname)
        self.color= "green"

class MarutiEsteem(Vehicle):
    
    def __init__(self, fname, num_wheels):
        super().__init__(fname)
        self.color = "blue"
        self.wheels = num_wheels

class Wheels:
    number_of_wheels_car = 4
    number_of_wheels_truck = 6
    number_of_wheels_motorcycle = 2

veh_1 = Vehicle("four wheeler")
c_1 = Car("second four wheeler", 4)
m_1 = MarutiEsteem("a", 4)

print("Vehicle:", id(veh_1))
print("Car:", id(c_1))
print("Maruti Esteem:", id(m_1))

print(veh_1.color)
print(veh_1.name)
print(c_1.color)        
# creating wheels object
# Wheels is a composition class
wheels = Wheels
print(wheels.number_of_wheels_car)
print(c_1.name)
c_1.horn()
print(m_1.color)