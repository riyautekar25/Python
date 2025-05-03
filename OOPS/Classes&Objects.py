'''
class- is a blueprint for an object
Object- instance of a class

class has two attributes/variables
class variables : same for all instances
instance variable : when object is instantiated, the instance varibles for each object gets created
modifying value of class variable will change its value for all objects
however modifying value of instance variable say changing value of var1 of obj1 will not change value of var1 of obj2 as they both are completely independent of each other.

__init__(): Act as a constructor (such as default const in Java/c), allocates memory to objects.
It initializes the attributes of the class.
self keyword: references to attribute of currect object
'''
class Car:
    wheels=4 #class Attribute
    def __init__(self,name):
        self.name = name # instance attribute

car1 = Car("Kia")  
print(car1.name, car1.wheels)
car1.name="Tata"
print(car1.name, car1.wheels)
car2=Car("Nissan")
car1.wheels=2 #class variable can not be modified using object
print(car2.name, car2.wheels)
Car.wheels=2 #so we use class to modify class variables
print(car2.name, car2.wheels)