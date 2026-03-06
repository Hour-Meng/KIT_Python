# In this we will learn more about pyton inheritance 

class Parent():
    def __init__(self,name: str, address: str):
        self.address = address
        self.name = name

    # the inheritance part

    def owning_car(self):
        print("You got a car")
    
    def owning_moto(self):
        return ("You own a moto")

main = Parent("Boss", "PPK")

# pass in the Parent class into child
# to inherite from Parent you need to use super function, also you need to pass in the argument that are require in Parent(name, address)
class Child(Parent):
    
    def __init__(self, name, gender): # This is the body structure of the child itself
        super().__init__(main.name , main.address) # super is a special connection to connect to it's parent

        self.name  = name
        self.gender = gender

child1 = Child("Mina", "Male")

print(child1.owning_moto())


# You can import it from other file as well
from other_inheritance import other_Parent
from other_inheritance import other_P   # Rather than filling the argument of parent in, we can just give it then import it
other_P = other_Parent("Bam", "TTK")

class other_Child(other_Parent):
    def __init__(self, name, gender): # 
        super().__init__(other_P.name, other_P.address) # 
        self.name = name
        self.gender = gender

other_child1 = other_Child("Batdo", "Female")
other_child2 = other_Child("Peanut", "Male")

print(other_child2.do_own_car())
# The output is 
"""
This guy also own a car
None
"""
# To not see the None, just use return instead of print
print(other_child1.do_own_moto())

from other_inheritance import other_Parent2 # go check other_Parent2 it's important

class other_Child2(other_Parent2):
    def __init__(self, name, gender):
        super().__init__() # Since the parent class already have the name and address, we don't need to pass in the argument
        self.name = name
        self.gender = gender

other_child3 = other_Child2("Peanut", "Male")
print(other_child3.address) # access the address from parent
# note that if you call other_child3.name ( it will return the child name instead of the parent's name ) local is superior
print(other_child3.do_own_car())