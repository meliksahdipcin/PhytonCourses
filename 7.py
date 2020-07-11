# %% Final Project

"""
OOP: Object Oriented Programming
    - Class / Object
    - Attributes / Method
    - Encapsullation / Abstraction
    - Inheritance
    - Overriding / Polymorphism
"""

from abc import ABC, abstractmethod

class Shape(ABC):
    # Shape = Super Class / Abstract Class
    
    # abstract method
    @abstractmethod
    def area(self): pass

    @abstractmethod
    def perimeter(self): pass

    # overriding and polymorphism
    def toString(self): pass

class Square(Shape):
    # Sub class / child
    
    # encapsullation
    def __init__(self, edge):
        self.__edge = edge
        
    def area(self):
        result = self.__edge ** 2
        print("Square area = ", result)
        
    def perimeter(self):
        result = self.__edge * 4
        print("Square perimeter = ", result)
        
    # overring / polymorphism
    def toString(self):
        print("Square edge = ", self.__edge)
        
class Circle(Shape):
    # Sub class / child
    
    # constant variable
    pi = 3.14
    
    # encapsullation
    def __init__(self, radius):
        self.__radius = radius
        
    def area(self):
        result = self.__radius ** 2 * self.pi
        print("Circle area = ", result)
        
    def perimeter(self):
        result = 2 * self. pi * self.__radius
        print("Circle perimeter = ", result)
        
    # overring / polymorphism
    def toString(self):
        print("Circle radius = ", self.__radius)
        

s = Square(5)
s.area()
s.perimeter()
s.toString()

c = Circle(5)
c.area()
c.perimeter()
c.toString()

















