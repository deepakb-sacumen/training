class Vehicle:
    def __init__(self, fname):
        self.name = fname
        self.color = "red"
    
    def horn(self):
        print("peep peep")

class Wheels:
    def __init__(self, num_of_wheels):
        self.num_of_wheels = num_of_wheels

class Car(Vehicle,Wheels):
    def __init__(self, fname, num_wheels):        
        super().__init__(fname)
        self.color= "green"
        super().__init__(num_wheels)


class MarutiEsteem(Vehicle, Wheels):    
    def __init__(self, fname, num_wheels):
        super().__init__(fname)
        self.color = "blue"   
        super().__init__(num_wheels)       

     
    

veh_1 = Vehicle("four wheeler")
c_1 = Car("second four wheeler", 4)
m_1 = MarutiEsteem("a", 4)


print("Vehicle:", id(veh_1))
print("Car:", id(c_1))
print("Maruti Esteem:", id(m_1))

print(veh_1.color)
print(veh_1.name)
print(c_1.color)        
print(c_1.num_of_wheels)
print(c_1.name)
c_1.horn()
print(m_1.color)