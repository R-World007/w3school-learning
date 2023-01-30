# print all items in the list, one by one
list1= ["apple","banana","cherry"]
for x in list1:
    print(x)

# loop through the index Numbers
# range() and len()
list2 = ["Hi","Hello","Hey"]
for i in range(len(list2)):
    print(list2[i])
    
# while loop
list3 = ["Happy","Joy","Pleasure"]
i = 0
while i < len(list3):
    print(list3[i])
    i = i + 1

list4 = ["apple","banana","cherry"]
[print(x) for x in list4]

