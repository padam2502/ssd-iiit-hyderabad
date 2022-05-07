# parent class
class Vehicle():
    def __init__(self, color):
        self.color = color
    def getcolor(self):
        return self.color

# subclass
class Car(Vehicle):
    def __init__(self, color, model):
        Vehicle.__init__(self, color)
        self.model = model

    def getmodel(self):
        return self.model
  

# create an object of class

c = Car("Red","Audi")
print(c.getmodel(), c.getcolor())
print(c.color)

