## YOu have to find if a string entered by the user is a palindrome or not

org_string = input("enter a string")
reversed_string = org_string[::-1]
if org_string==reversed_string:
    print("WOOW The given sring is a pallindrome!!!")
else:
    print("Pleese Try again")


