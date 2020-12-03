# Find the sum of all Integers from 1 to n  without using loop/ and using loop

## without loop

n = int(input("Enter the Value "))
print(sum(list(range(1,n))))

## with the loop
print("with loop")
sum = 0
for i in range(1,n+1):
    sum += i
    print(sum)