# What is OOP?

# OOP stands for object oriented program


#Introduction to Object Oreinted Programming

'''
OOP is programming design paradigm that a class is template /blueprints for creating Objects.
    + A class is like a blueprint for creating objects.
    + An object has properties and methods(functions) associated with it.
    + Almost everything in Python is an object
'''
#Case study to store information about a person. using List
def user_profile():

    people = ["Name: Jonh Doe, Email: jonhdoe@example.com, age: 32", "Name: Vann Makara, Email: vann.makara@example.com, age: 25"]

    return people



# 1. call
user1 = user_profile()[0]
user2 = user_profile()[1] # or [-1]
print(user1)
print(user2)

# 2. create a class: UserProfile
class UserProfile:
    def __init__(self, name: str, occupation: str, age: int, height: int | float, dob: str, phone_number: str, is_married: bool):
        self.name = name
        self.occupation = occupation
        self.age = age
        self.height = height
        self.dob = dob
        self.phone_number = phone_number
        self.is_married = is_married
    
    def greet(self):
        print(f"Hello my name is {self.name} my job is {self.occupation} and I am {"Maried" if self.is_married else "single"}.")

user3 = UserProfile("Bob", "SE", 25, 1.70, "02/10/2000", "01982411", True)
user4 = UserProfile("Drake", "SE", 21, 1.81, "02/03/2000", "01952411", False)

print(user4.greet())
print(user3.greet())

