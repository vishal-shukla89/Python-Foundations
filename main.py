#print('namaste python')
#print(18+2121)

#1.accept an inte and print hello world n times
# n=int(input("Enter an integer:- "))
# for i in range(n):
#     print("Hello World")

# #2.print natural numbers upto n
# n=int(input("Enter An integer where you want to print natural numbers: "))
# for i in range (1,n+1):
#     print(i)

# #3. print n to 1
# n=int(input("Enter your value of n :- "))
# for i in range(n,0,-1):
#     print(i)

#4. take an iput n and make its table 
# n=int(input(" enter an iteger to print its  table:- "))
# for i in range(1,11):
#     print(f"{n}*{i}={n*i}")

# #5. get the sum upto n natural numbs
# n=int(input("Enter the value of n :- "))
# sum=0
# for i in range(1,n+1):
#     sum+=i

# print(f"sum of {n} natural nubs is {sum}")

# #6. to tske input n then find n!
# n=int(input("Enter the value of n to fint its factorial:- "))
# fact=1
# for i in range(1,n+1):
#     fact*=i

# print(f"factorial of {n} is {fact}")

# #7. find the sum of all even and odd numbers upto n seperately
# n=int(input("enter the value of n:- "))
# even=0
# odd=0
# for i in range(1,n+1):
#     if i%2==0:
#         even+=i
#     else:
#         odd+=i
# print(f"sum of all even and odd numbers upto {n} is {even},{odd} ")

#8.to check number is perfect or not
# n=int(input("Enter the Value of n :- "))
# sum=0
# for i in range(1,n):
#     if n%i==0:
#         sum+=i
# if n==sum:
#     print(f"the number {n} is Perfect Number")
# else:
#     print(f"the number {n} is not Perfect Number")

#9.check num is prime or not
# n=int(input("Enter the value of n:- "))
# count=0
# for i in range(1,n+1):
#     if n%i==0:
#         count+=1
# if count==2:
#     print(f"the number {n} is Prime NUmber")
# else:
#     print(f"the Number {n} is not Prime")

#10. print string in revrse 
#a)with function
# a="sher"
# print(a[::-1])
#b)without fun that is with for loop
# a="sher"
# b=""
# for i in range(len(a)-1,-1,-1):
#     b=b+a[i]
# print(b)

#11. to count nos of digits , alphas, symbols in string
# n=input("Enter your string:- ")
# dig=0
# alph=0
# sym=0
# for i in n:
#     if i.isdigit():
#         dig+=1
#     elif i.isalpha():
#         alph+=1
#     else:
#         sym+=1
# print(f"The number of digits are {dig}\nThe number of alphabets are {alph}\nThe number of symbols are {sym}")

#11.to create a game of guessing numbs between 1 to 100
# import random
# num=random.randint(1,10)
# tries=0
# while True:
#     guess=int(input("enter your gessed number betwwen 1 to 10:- "))
#     if num==guess:
#         tries+=1
#         print(" congratulations, you got the correct guess in ",tries,"tries !")
#         break
#     elif num<guess:
#         tries+=1
#         print("Try a number little LOWER")
#     elif num>guess:
#         tries+=1
#         print("try a number little HIGHER")
#     else :
#         tries+=1
#         print("Unfortunately u guessed Wrong Number")


# a=input("Enter your word :- ")

# def palli(a):
#     var=""
#     for i in range(len(a)-1,-1,-1):
        
#         var=var+a[i]
        
#     print(var)
    
#     if var==a:
#         print(f"the word {a} is a Pallindromic word")
#     else:
#         print(f"the word {a} is not a Pallindromic word")

# print(palli(a))

# a=[1,2,3]
# a[0]=4
# print(a)

#using .append() method
# a=[1,2,3,4,5]
# a.append(6)
# print(a)

#using .insert() method to insert value inbetween
# a=[1,3,4,5]
# a.insert(1,2)
# print(a)
# b=a.pop(1)
# print(a)
# print(b)

# a=[1,2,2,2,3,2,2,4,2,3,2]
# print(a.count(2))
# a=[1,3,2,4,5]
# a.sort()
# print(a)
# a.reverse()
# print(a)
# a.clear()
# print(a)

#14. print positive and negative numbers seperately from the list
# a=[1,-1,2,-2, 3,-3,4,-4]
# b=[]
# c=[]
# for i in a:
#     if i>=0:
#         b.append(i)

# print(f"Positive numbers are {b}")
# for i in a:
#     if i<0:
#         c.append(i)

# print(f"Negative Numbers are {c}")


#15.mean of the list
# a=[12,32,32,43,21,34]
# sum=0
# for i in a:
#     sum+=i

# print(f"the mean of the list {a} is {sum/len(a)} ")

# #16.find the greatest no and its index too
# a=[1,22,32,4,35,56,65,43]
# max=0
# ind=0
# for i in range(len(a)):
#     if a[i] >= max:
#         max=a[i]
#         ind=i
# print(f"Greatest value of the list {a} is {max} and its index is {ind}")

# #17. find the second greatest element 
# a=[12,32,32,12,32,11,34,56,45]
# max=0
# s_max=0
# for i in a:
#     if i>=max:
#         s_max=max
#         max=i
#     elif i>s_max:
#         s_max=i
# print(f"1st greatest number is {max} and second Greatest number is {s_max}")

# #18. check if the list is sorted or not (i.e., in ascending order)
# #mine method
# a=[1,2,3,5,2,3]
# old=a.copy()
# a.sort()
# if old==a:
#     print(f"The given list {old} is  already sorted")
# else:
#     print(f"The given list {old} is not sorted ,where its sorted version is {a}")
#2nd method 
# a=[1.4,66,75,4,3,55,3,66,78,2]
# for i in range(len(a)-1):
#     if a[i]<a[i+1]:
#         continue
#     else:
#         print(f"your list {a} is not sorted")
#         break
# else:
#     print(f"your list {a} is already sorted")

#19.list,tuples
# a={1,2,3,4,5}
# a.add(6)
# print(a)
# b=a.copy()
# a.clear()
# print(a)
# print(b)

#20.setmethods between two sets
# a={1,2,3,4,5,6,7}
# b={5,6,7,8,9,10,11}
#normal method
# c=a.union(b)
# d=a.intersection(b)
# e=a.difference(b)
# f=a.symmetric_difference(b)
#shortcut method
# c=a|b
# d=a&b
# e=a-b
# f=a^b
# print(f"union of two sets is {c}")

# print(f"intersection of two sets is {d}")

# print(f"diffference of two sets is {e}")

# print(f"symmetrc difference between two sets is {f}")

# print(dir(dict))

#using methods of dctonary 
# a={1:10,2:10,3:30}
# a[2]=20    #reassigning values to keys
# a[4]=40    #creating new key:value pair inside dict
# print(a)
# copy=a.copy()

# a.update({5:50,6:60})  #adding new dictionary
# c2=a.copy()
# print(f"befor update-{copy} and now after update- {c2}")

# del a[6] #used to delete value with this whole pair gets deleted
# print(a)

# a={1: 10, 2: 20, 3: 30, 4: 40, 5: 50}
# # d2=a.get(5)
# # print(a)
# # print(d2)
# d3=a.popitem()
# print(d3)
# print(a)
# c=a.pop(4)
# print(c)
# print(a)

#21. write code to merge two dictionary short and long method 
# a={1:10,2:20,3:30}
# b={4:40,5:50,6:60}
# #short method
# # a.update(b)
# # print(a)
# #long method
# for i in b:
#     a[i]=b[i]  #creating new key :value pair inside a
# print(a)

#22. to sum all the values in dictionary 
# a={1:10,2:20,3:30,4:40}
# sum=0
# for i in a:
#     sum=sum+a[i]
# print(f"The SUM of all the values of dictionary is {sum}")

# #23. find the frequency of numbers in list and then make dictionary in format {num:freq}
# a=[1,2,1,2,3,4,5,6,7,6,5,4,3,2,1,2,6,5,4,8,9,8,7,6]
# d={}
# for i in a:
#     if i in d.keys():
#         d[i]+=1
#     else:
#         d[i]=1
# print(d)

# #24.combine two dict. and for same keys in both add corresponding values
# a={1:10,2:20,3:30,4:43}
# b={4:40,5:50,6:60}
# for i in b:
#     if i in a.keys():
#         a[i]=a[i]+b[i]
#     else:
#         a[i]=b[i]

# print(a)


##EXCEPRION HANDLING
# #25. using try,except,else to get
# a=int(input("Enter the number:- "))
# try:    #it wraps the error or exeption so the next line of code ca run , but it only works if it is with except or finally or both
#     print(10/a)
# except Exception as err:
#     print(f"ohh, you got the error and th error is {err}")#it handles the exception given by try
# else:
#     print("you got no error so far") #else will run if except doesnt works means if there are no error or evception
# print("i have done the division")     #to check if last line runs or not


#29.using finally (it will no matter what if errorr or except or else)

# a=int(input("Enter the number:- "))
# try:    #it wraps the error or exeption so the next line of code ca run , but it only works if it is with except or finally or both
#     print(10/a)
# except Exception as err:
#     print(f"ohh, you got the error and th error is {err}")#it handles the exception given by try
# else:
#     print("you got no error so far") #else will run if except doesnt works means if there are no error or evception
# finally:
#     print("i will run no matter what ")

# print("i have done the division")     #to check if last line runs or not

##FILE HANDLING
#30. to use open()function then read it 
# after that create new file named superman 
#then add 1st line then after that append one more line toit

# a=open(r"C:\Users\visha\Downloads\AI_INSTRUCTOR_GUIDE.md")
# b=a.read()
# print(b)


# # 1. Open the file in Write ('w') mode
# a = open("superman.txt", 'w')
# a.write("this my first line")
# a.close() # Save and close

# # 2. Re-open the file in Read ('r') mode
# b = open("superman.txt", 'r')
# print(b.read()) # Now you can safely read and print it
# b.close() # Always close when you're done!
a = open("superman156.txt", 'w')
a.write("this my first line")
a.close()