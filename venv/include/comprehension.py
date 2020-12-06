## Given two Lists, make a new list which contains the elements present in list1,list2

# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7,8 ]
# list3 = [i for i in list1 if i in list2]
# print(list3)

## List1 has length 3,list2 has length 6

list1 = [1,2,3]
list2 = [2,3,4,5,6]
list3 = [i for i in list1 if i in list2]

print(list3)