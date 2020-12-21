## I have to get an integer from the user

a = input("Enter a number")
if a.isdigit():
    print("Whoa is a number")

else:
    raise ValueError