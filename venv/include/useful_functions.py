##sum(),sorted(),max(),min()
##[1,2,3,4,5] = [1,4,9,16,25]

'''
squares=[]
numbers = [1,2,3,4,5]
for i in numbers:
   j=i*i
   squares.append(j)

   print(squares)

'''

#map(function,sequence)

# print(list(map(lambda  x:x*x,[1,2,3,4,5])))
list1 =[1,2,3,4,5]
list2 =[6,7,8,9,10]
print(list1 + list2)

##we want it to be printed as a tuple ie [(1,6) ......]

print("getting the values as a tupple")
print(list(zip(list1,list2)))

## filter functions -> filters every element in a function
print("filtering the every element in a function and checking if its an event number")
print(list(filter(lambda x:x%2==0 , [1,2,3,4,5,6,7,8,9,10])) )

