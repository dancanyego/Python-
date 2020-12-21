class Car:
    def __init__(self , millage ,color):
        self.millage=millage
        self.color=color

    def getMillage(self):
        return self.millage

    def getColor(self):
        return self.color

    def greet(self):
        print("yoo Car")


model1 = Car(55 , "Red")
model2 = Car(24 , "Yellow")

print(model1.getMillage())
print(model2.getMillage())
print(model1.greet())