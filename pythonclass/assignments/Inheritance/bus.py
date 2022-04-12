class Vehicle:
    def __init__(self, name, maxSpeed, mileage):
        self.name = name
        self.maxspeed = maxSpeed
        self.mileage = mileage
    
    def capacity(self, capacity):
        #dont do self.capacity = capacity cuz youre just using it locally
        #if you were to use this globally you would need to 
        return f"this vehicle has {capacity} seats"
        
highlander = Vehicle("no", 160, 120000)
print(highlander.maxspeed)
print(highlander.mileage)

class Bus(Vehicle):

    def __init__(self, name, maxSpeed, mileage):
        Vehicle.__init__(self, name, maxSpeed, mileage)


    def getCap(self, capacity):
        return f"the capacity is {capacity}"

    def capacity(self, capacity = 50): #make the name the same in parent and child class
        return super().capacity(capacity = 50)

schoolbus = Bus("volvo", 100, 12000)
print(schoolbus.capacity(90))
print(schoolbus.getCap(80))