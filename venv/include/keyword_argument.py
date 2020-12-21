## Solving thr quadratic equation eg ax**2+bx+c = 0
import math
def quadratic(b,c,a):
    determinant=math.sqrt(b*b-4*a*c)
    x1=(-b+determinant)/(2*a)
    x2 = (-b + determinant) / (2 * a)
    return x1,x2
    # x1 = -b+sqrt(b*b-4*a*c)/2*a
    # x2 = -b + sqrt(b * b - 4 * a * c) / 2 * a
## Returning arguments
## X**2+5*x+6=0
root1,root2 = quadratic(a=1,b=5,c=6)
# print(root1,root2)
print("x1: "+str(root1))
print("x2: "+str(root2))


