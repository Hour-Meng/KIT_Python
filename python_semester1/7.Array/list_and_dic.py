# We have already learn about dictionary and list
# What if we want to combine them together?
# The combine of list and dictionary will result in a .json file
# .json file is a file format that is used to store data in a structured way

person = []
person1 = {"name":"Horu", "age":21, "is_cool": True}
person2 = {"name":"Debby", "age":20, "is_cool": False}

person.append(person1)
person.append(person2)

#=== to print person 1 data ===
print(person[0])
#=== to access key of person1 ===
print(person[0]["name"])
#=== to print only key of person1 ===
print(person[0].keys())
#=== to print only the value of person1 ===
print(person[0].values()) # you still can convert it into list and more


