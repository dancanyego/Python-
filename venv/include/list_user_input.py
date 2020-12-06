## This will help us to get the comprehension when a user inputs a new list
# using for loop
new_list=[]
n = int(input("Enter The Size of The List"))
print("Enter The Values One by one")
for i in range(0,n):
    a = input()
    new_list.append(a)

print(new_list)
