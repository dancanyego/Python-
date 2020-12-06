## we will be checking on the scope function

def update(x):
    x = 10
    print("Inside function:" +str(x))

x = 5
print("outside function:" +str(x))
update(x)  #our x is 5
print("After executing the function,the value of x:" +str(x))
