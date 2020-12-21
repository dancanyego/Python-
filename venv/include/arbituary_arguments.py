# arbituary arguments -> when you bare uncertain about two numbers

# def add(x, y):
#     return x+y+z
# add(x=10 ,y =10)

def add(*x):
    print(x)
    print(type(x))
    return sum(x)

add(10,20,30,40,50)