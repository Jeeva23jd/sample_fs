# print("Welcome")
# name = "Jeeva"
# age = 21
# height = 155.2
# is_student = True
# print(name,"\n",age)
# n1 = name.upper()
# print(n1)
# list = ["apple","Orange"]
# list.append("kiwi")
# print(list)
# print(name[0])
# print(len(name))
# num1=45
# num2=-100
# num3=0
# bignum=12345678900987654312
# print(bignum)
# result=None 
# print(result)
# print(type(result))
# fruits=['apple','banana','papaya']
# mixed=[5,'Jeeva',7.9,True]
# print(mixed[-3])
# tuple=(10,20,30,40)
# x = tuple
# print(x)
# a,b,c,d=x
# print(a,"\n",b)
# #using tuple as dictionary key
# map = {(0,0):"origin",(1,1):"diagonal"}
# print(map[0,0])
# print(map)
# colors ={'pink','red','violet'}
# colors.add('Blue')
# colors.remove('red')
# print(colors)
# set1={1,2,3,4,5}
# set2={3,5,6,8}
# print(set1|set2) #union
# print(set1&set2)
# print(set1-set2)
# fs = frozenset([1,2,3,45])
# print(fs)
# s={"a",'b','c'}
# f=frozenset(s)
# print(f)
# print(f"5+3 = {5+3}")
# print("5-3 =",(5-3))
# a=[1,2,3]
# b=[1,2,3]
# print(a==b)
# print("a is b",a is b)
# x=5
# x*=2
# print(x)
# x-=2
# print(x)


# age=int(input())
# if age < 13:
#     print("child")
# elif age<18:
#     print("teenage")
# else:
#     print("adult")


# fruits=['banana','apple','orange']
# for f in fruits:
#     print(f)
# for i in range(5):
#     print(i,end=" ")
# for i in range(10):
#     if i==3:
#         continue
#     if i==7:
#         break
#     print(i,end=" ")


# count=0
# while True:
#     print(count)
#     count+=1
#     if count >=5:
#         break


# print("Multiplication table :")
# for i in range(1,4):
#     for j in range(1,10):
#         print(f"{i}x{j}={i*j}")
#     print()


# def greet(name):
#     m=f"Hello ,{name}"
#     return m
# print(greet("Jeeva"))
# def add(a,b):
#     return a+b
# result=add(55,5)
# print(result)
# def multable(num):
#     for i in range(1,11):
#         print(f"{num}x{i}={num*i}")
# a=int(input("Enter a number"))
# multable(a)
# global_var=10
# def func_with_scope():
#     local_var=20
#     print(f"Local:{local_var}")
#     print(f"global:{global_var}")
# func_with_scope()
# print(f"Global:{global_var}")

# print('a','b','k',sep="-")
# print('a','b','k',sep="|")

# numbers = list(range(10))
# print("original:",numbers)
# print("first 3:",numbers[:3])
# print("from index 5:",numbers[5:])
# print("middle:",numbers[3:5])
# print("every second element:",numbers[::2])
# print("Reversed:",numbers[::-1])
# print("last 3:",numbers[-3:])

# flowers=['lily','lotus','jasmine']
# flowers.append('rose')
# print(flowers)
# flowers.insert(2,'daizy')
# print(flowers)
# flowers.pop()
# print(flowers)
# flowers.remove('jasmine')
# print(flowers)
# print(flowers.pop(0))
# print(flowers)
# numbers=[3,1,4,1,5,9,8,6]
# num_copy=numbers.copy()
# print(num_copy)
# numbers.sort()
# print(numbers)
# numbers.sort(reverse=True)
# print(numbers)
# listcount=numbers.count(1)
# print(listcount)
# index=numbers.index(5)
# print(index)
# k=['a','b','c']
# k.clear()
# print(k)

#string methods
# text ='Welcome to Python!'
# print(text[0])
# print(text[-1])
# print(len(text))
# print(text[::-1])
# print(text.upper())
# print(text.lower())
# print(text.capitalize())
# print(text.title())
# #remove whitespace
# text1=" Hello ! "
# print(text1.strip())
# txt2=" Hello"
# print(txt2.lstrip())
# txt3="Hello "
# print(txt3.rstrip())

# string = "apple,banana,orange"
# fruits=string.split(",")
# print(fruits)

# joined="-".join(fruits)
# print(joined)

# try:
#     result =10/0
# except ZeroDivisionError:
#     print("cannot divide by zero")

# try:
#     int("abc")
# except ValueError:
#     print("valueerror cannot convert 'abc' to integer")

#class and object
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
p1=person("Jeeva",20)
p1.greet()

#type casting
print(int(3.14))