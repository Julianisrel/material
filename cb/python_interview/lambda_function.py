# def double(n):
#     return n*2


# lambda funciton 

from turtle import clear


double = lambda n:n*2
# print(double(10))



larger = lambda a,b:a if a>b else b 
# if a is greater than b otherwise i'll return b 
# print(larger(10,47))

names = ["Alan", "Gregory", "Zlatan", "Jonas", "Tom", "Augistine"]

names.sort(key = lambda x:len(x))

# print(names)

# Passing variables between functions 
def funa():
    name=input("what is your name?")
    age=input("what is your age?")
    return name, age



def funb():
    name, age=funa()
    print(name)
    print(name)

funb()

# map() function 
list = [1,2,3,4,5,678,8]


def fun(x):
    return x**x
   
newList = []
for x in list:
    newList.append(fun(x))

print(newList)
