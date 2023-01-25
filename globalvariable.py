# create the variable outside of a function, and use it inside the function

x = "Great"

def myfunc():
    print("python is "+ x)

myfunc()

#Create a variable inside a function, with the same name as the global variable

a = "Good"

def myf():
    a = "awesome"
    print("Python is "+ a)

myf()

print("Python is " + a)

# global Keyword

def myp():
    global b
    b = "well"

myp()
print("Python is "+ b)


c = "GoodJob"

def myl():
    global c
    c = "fantastic"

myl()
print("Python is "+ c)
