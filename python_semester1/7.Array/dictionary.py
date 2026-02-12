# We will learn about dictionary in python
# In dictionary it store data in "key" and "value" pair

# what is a list? 
# A list is defined by curly bracket {}, it can't be duplicate, it can store any datatype such as, str, int, bool, list, tuple...

person = {"name":"Meng", "age":21, "no-girl":True, "employed":False}

# to get the value from key
print(person["name"])
print(person["age"])

# === to get all of the key ===

print(person.keys()) # the value you will be getting is in a dictionary
                    # You can convert it in to list or tuple as you like
print(list(person.keys())) 
# you can verity the data type, to know is it actually a list or not
print(type(list(person.keys()))) # The output will be <class "list">

# the process on turning datatype is called "casting"

# or maybe you can convert it into a tuple
print(tuple(person.keys()))

#==== to get the value ====
print(person.values()) # which you can do the same, turn it into list or tuple later

#=== copy the dictionary ===
copy_dictionary = person.copy()
print(copy_dictionary) # now this value is copy

#=== editing value ===

person["age"] = 22  # the orinal age was 21 and now it has changed to 22 instead

#=== deleting the key ===
person.pop("age") # this will delete age key which will also delete it's value


#=== Getting every key and value in dictionary ===

for i, (key, value) in enumerate(person.items()):
    print(f"{i+1}.{key} =  {value}")
