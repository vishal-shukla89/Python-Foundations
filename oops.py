# #1.BAsic example of OOPS 
# class Factory:
#     a=12  #Attribute 
#     def hello(self):  #Method
#         print("How are you")
# print("I HAVE BEEN INITIALIZED !!")

# print(Factory().a)
# Factory().hello()

# #2.DOing WITh object
# class Factory:
#     a=12  #Attribute 
#     def hello(self):  #Method
#         print("How are you")
# print("I HAVE BEEN INITIALIZED !!")

# obj=Factory()  #OBject created 
# print(obj.a)
# obj.hello()

# #3.BASIC example for self to target object location and take its arguments
# class Factory:
#     def __init__(self,material,zips,pockets):
#         self.material=material
#         self.zips=zips
#         self.pockets=pockets
#     def show(self):
#         print(f"your object details are {self.material},{self.zips},{self.pockets}")

# reebok=Factory("Leather",2,3)
# campus=Factory("NYLON",3,4)
# reebok.show()

# #4.to show the examples of types of attributes and methods
# class Animal:
#     name="Lion"  #class attribute
#     def __init__(self,age):
#         self.age=age       #instance attributr
    
#     def show(self):            #instance method
#         print(f"hello animal is {self.name} and age is {self.age} ")
    
#     @classmethod
#     def hello(cls):
#         print("hello this is classmethod")

#     @staticmethod
#     def static():
#         print("hello this is static method ")

# obj=Animal(12)
# obj.show()
# obj.hello()
# obj.static()

# #5.inheritance basic example
# class Parent:
#     def speak(self):
#         print("I can speak")
# class Child(Parent):
#     pass
# obj=Child()
# obj.speak()

# #6.constructor in inheritance basic example
# class Parent:
#     def __init__(self,name):
#         self.name=name
 
# class Child(Parent):
#     def speak(self):
#         print(f"I am {self.name}")

# obj2=Child("Vishal")
# obj2.speak()

# #7.use of super() function which targets parent class
# class Animal:
#     def __init__(self,name):
#         self.name=name
#     def show(self):
#         print(f"My name is {self.name}")
# class Child(Animal):
#     def __init__(self, name,age):
#         super().__init__(name)
#         self.age=age
#     def show(self):
#         print(f"My name is {self.name} and age is {self.age}")

# obj1=Animal("lion")
# obj2=Child("monkey",23)
# obj1.show()
# obj2.show()

# #8.three ways of achieving polymorphism but in python it has only two ways
# #i)method overloading ---- but in pythis this the only way that doesnt works
# class Family:
#     def __init__(self):
#         print(" iam old parameter method")
#     def __init__(self, name):
#         self.name=name
#         print("this is new parameter method")
# ob=Family()  # it is asking for name means the method is overwritten

# #ii)method overiding means same method will be overwritten by child class
# class Family:
#     def show(self):
#         print("I AM THE BEST")

# class Child(Family):
#     def show(self):
#         print("I AM ALWAYS THE BEST")

# obj=Child()
# obj.show()   # see you will get ouput of child class as it is overwritten

# #iii) duck typing in this we can make two methods same in different classes and the output will not be overwritten 
# class Family:
#     def show(self):
#         print("i am the best")
# class Child:
#     def show(self):
#         print("I am the samrtest")

# obj=Family()
# obj2=Child()
# obj.show()
# obj2.show()


# #9.example of abstraction
# #in this make an abstraction class which includes area and perimeter method 
# #so other subclass should also include this
from abc import ABC,abstractmethod

class Absrtact(ABC):
    @abstractmethod
    def Perimeter(self):
        pass
    @abstractmethod
    def Area(self):
        pass

class Square(Absrtact):
    def __init__(self,side):
        self.side=side
    def Perimeter(self):
        print(f"Perimeter of the square is {4*(self.side)}")
    def Area(self):
        print(f"Area of square is {(self.side)**2}")

class Circle(Absrtact):
    def __init__(self,radius):
        self.radius=radius
    def Perimeter(self):
        print(f"Perimeter of circle is {2*(22/7)*(self.radius)}")
    def Area(self):
        print(f"area of Circle is {(22/7)*(self.radius)**2}")


obj1=Square(5)
obj2=Circle(5)
obj1.Area()
obj1.Perimeter()
obj2.Area()
obj2.Perimeter()



