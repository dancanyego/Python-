## x+iy -> complex number
class ComplexNumber:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    def __str__(self):
        return "{}+i{}".format(self.real, self.img)

    def __add__(self, other):
        x=self.real+other.real
        y=self.real+other.img
        return "{}+i{}".format(x,y)

num1=ComplexNumber(5,2)
num2=ComplexNumber(10,20)
print(num1)
print(num2)
print(num1+num2)