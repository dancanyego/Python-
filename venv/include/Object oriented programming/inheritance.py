class Animal:
    def __init__(self,color):
        self.color=color
    def introduce(self):
        print("Hello am an animal")

    def makesound(self):
        print("uuuuuiiii")

class Dog (Animal):
    def takecare(self):
        print("I Am Coming you animals")
class Cat(Animal):
    def makesound(self):
        print("MEaaaw ")
wild_animal = Animal("Brown")
poppi = Dog("white")
kitten = Cat("White")
wild_animal.makesound()
kitten.makesound()

poppi.takecare()