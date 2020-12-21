import random
letters=[chr(i) for i in range(35,125)]
password=""
length=int(input("Enter the Length"))
for i in range(0,length):
    password=password+random.choice(letters)

print(password)