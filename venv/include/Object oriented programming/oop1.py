class Students:
    def __init__(self,name,age): ## constructor definition
        self.sname=name
        self.sage=age
        print("Yoo Bazu My name is {} and my age is{}".format(self.sname,self.sage))

        ## self will refer to the current object
##creating objects of the class

student1 =Students("Jonte" , 19)
student2 =Students("Plimo" , 52)

##object_name = class_name()
## Creating an object of a class -> Instantiating a class(Instatiation)
student3 = Students("Chemosi" ,29)
student4 = Students("Chemoget" ,62)
print(type(student3))