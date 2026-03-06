# In this part we will learn about abstraction with python turtle

import turtle as t
from abc import ABC, abstractmethod
# abc stands for abstraction based class

shape = t.Turtle()

class Shape(ABC):
    @abstractmethod
    def drawable(self):
        pass
    
    @abstractmethod
    def modify_shape(self):
        pass

# The abstract method will leave an error if the child did not use all of the it's abstraction method

class Rectangle(Shape):
    def drawable(self):
        for i in range(4):
            shape.forward(100)
            shape.left(90)

    def modify_shape(self): # This mean that since modify_shape is also part of the abstract method
        pass                # If I don't use this function in Rectangle, it will leave an error
            
rec1 = Rectangle().drawable()
t.done()