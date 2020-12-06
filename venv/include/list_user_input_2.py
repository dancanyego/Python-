# using comprehension

n = int(input("Enter The Size of The List"))
print("Enter The Values One by one")

new_list=[input() for i in range(0,n)]
print(new_list)