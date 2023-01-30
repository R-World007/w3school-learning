fruits = ["apple","banana","cherry","kiwi","mango"]
newlist = []
for x in fruits:
    if "a" in x :
        newlist.append(x)
        
print(newlist)

fruit = ["app","Os","andriod","ios"]
list = [y for y in fruit if "a" in x]
print(list)

# newlist = [expression for item in iterable if condition == True]
list1 = ["apple","cherry","kiwi","orange"]
list1 = [z for z in fruits if z != "apple"]
print(list1)

# no if statement
list2 = [i for i in fruits]

# range()
list3 = [j for j in range(10)]
print (list3)

# only accept only numbers lower than 5
list4 = [n for n in range(10) if n < 5]
print(list4)
