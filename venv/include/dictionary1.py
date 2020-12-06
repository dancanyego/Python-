## to create a dictionary you have to use {}
details = {"name":"Jonte","Age":"29","Contact":"020202020202"}
print(details)

#Getting the age
# print(details["Age"])
# print(details["Contact"])

# adding values in the dictionary

details["blood_group"] = "B Positive"

# Changing values in the dictionary
details["name"] ="Umutiti"
print(details)
print(details.get("blood_group"))

# another way of creating a dictionary by using dict() function eg
# squares ={1:1,2:4,3:9}
squares = dict([(1,1), (2,4), (3,9) , (4,16)])  #Creating a list of tupple
print( squares)

