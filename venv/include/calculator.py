# infinite loop -> break
# it will loop untill break
while True:
    option = input("Enter 'add' or 'Subtract', 'multiply','divide', 'power' , quit' ")
    if option == 'quit':
        break
    elif option=='add':
        x = int(input("enter the first value"))
        y = int(input("enter the second Value"))
        print(x + y)

    elif option=='subtract':
        x = int(input("Enter the first value to subtract"))
        y = int(input("Enter the Second Value to subtract"))
        print(x-y)

    elif option=='multiply':
        x = int(input("Enter The First Value to Multiply"))
        y = int(input("Enter the Second Value to Multiply"))
        print(x*y)

    elif option=='divide':
        x = int(input("Enter the first value to divide"))
        y = int(input("Enter The second Value to divide"))
        print(x/y)

    elif option=='power':
        x = int(input("Enter the first value to power up"))
        y = int(input("Enter The second Value to power up"))
        print(x**y)

    else:
        print("Invalid argument!!!")


print("am out Thanks")
