## sorting the tuple pairs

list1 = [(1,2),(3,5),(111,45),(34,56)]
print("sorted on the order of the 1st element")
print(sorted(list1))

print("sorted on the order of the 2nd element")
sorted(list1,key=lambda x:x[1])