# #1.example of dunder methods by __init__,__str__ ,__add__
class Animal:
    def __init__(self,name,age):  #itll initialise attributes autometicaly
        self.name=name
        self.age=age
    def __str__(self):   #it will return this if object is called ,not location ,itll print value
        return f"Your Animals name is {self.name}"
    def __add__(self, other):  #itll  help to accss all the object and we can thenperform addition
        sum=0
        for i in other:
            sum=sum+i.age

        return f"the sum of ages is {self.age +sum}"

obj1=Animal("Lion",13)
obj2=Animal("monkey",15)
obj3=Animal("horse",24)
print(obj1+(obj2,obj3))
        
# #2.DECORATORS with wrapper
# #Basic example without any parameter
# def my_decorator(func):
#     def wrapper():
#         print("starting point before function runs")
#         func()
#         print("Ending line after function has been already run")
#     return wrapper

# @my_decorator
# def say_hello():
#     print("hello this line is of function")

# say_hello()

# #for one or two parameters
# def my_decorator(func):
#     def wrapper(a,b):
#         print("starting point before function runs")
#         func(a,b)
#         print("Ending line after function has been already run")
#     return wrapper

# @my_decorator
# def sum(a,b):
#     print(f"the sum is {a+b}")

# sum(22,31)

# #For multiple args use *args and **kwargs
# #a)
# def fun(*args,**kwargs):
#     print("Args:-",args)
#     print("Kwargs:-",kwargs)
# fun(1,2,3,4,name="vish",age=21)
# ##output_-Args:- (1, 2, 3, 4)
# #         Kwargs:- {'name': 'vish', 'age': 21}

# #b)create a function which can take multiple arguments and give sum of all
# def sumation(*args):
#     sum=0
#     for i in args:
#         sum=sum+i
#     print(sum)
# sumation(22,33,443,21,334,322,445,322,45,2322435,234543,223)
# ##output_-2559188

# #3.COMPHREHENSION method(one line code method)

# #a)List comphrehension (craete a list of even numbers between 1-20)
# l=[i for i in range(1,21) if i%2==0]
# print(l)
# #output_-[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# #b)Dictionary comphrehension(craete a dictionary which contains keys as 1-20 and values is squares of keys also do for even numbers)
# d={i:i**2 for i in range(1,21) if i%2==0}
# print(d)
# #output_-{2: 4, 4: 16, 6: 36, 8: 64, 10: 100, 12: 144, 14: 196, 16: 256, 18: 324, 20: 400}

# #c)Set comphrehension(create a set of evan numbs squares between 1-20)
# s={(i**2) for i in range(1,21) if i%2==0 }
# print(s)
# #output_-{64, 256, 100, 4, 36, 196, 324, 16, 144, 400}  #sice sets are inheritly unordered and the values get stored based on memory locatin i.e., hashing therefore the output is unordered

# #4.Lambda function (used to create one line code instead of multi line)
# addition=lambda a,b: a+b  #to show one line code which can add two numbers
# print(addition(12,56))

# check=lambda c: "even" if c%2==0 else "odd"  #create one line to show if the number is even or odd
# print(check(53))
# #output_-68
# #        odd

# #5.map(),filter() functions

# #a)using map(function,list) craete which takes values from list and perform same lambda or other functions operation on elements and gives final output list
# a=[1,2,3,4,5,6,7,8,9,10]
# square=map(lambda x: x**2,a)
# print(square)  #it gives only location of the object square
# print(list(square)) # list() converts that object into list
# #output_-<map object at 0x000001F29CCBFCC0>
# #        [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# #b)using filter(fun,list) create a function which filter out odd numbers and gives output as a list of even numbs
# a=[1,2,3,4,5,6,7,8,9,10]
# def even(x): #first way
#     if x%2==0:
#         return True
#     else:
#         return False
# check=filter(even,a)
# print(list(check))

# result=filter(lambda x:  True if x%2==0 else False,a) #second way
# print(list(result))
# # #output_-[2, 4, 6, 8, 10] for both output is same