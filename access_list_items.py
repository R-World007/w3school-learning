# acces them by referring to the index number
thislist= ['apple','orange','cherry']
print(thislist[1])

# Negative Indexing
# -1 refers to the last item, -2 refers to the second last item etc.
print(thislist[-1])
print(thislist[-2])

# Range of Indexes
mylists = ['apple','orange','cherry','berry','kiwi','avo',] # the first item is 0 index
print(mylists[2:5])

print(mylists[:4]) # 4 index number is not included in this case.

print(mylists[2:]) # start from index 2 number

# Range of Negative Indexes

print(mylists[-4:-1]) # -1 is not included but -4 is

# Check if item exists
list1 = ['hi','hello','happy',]
if 'hi' in list1:
    print("There is hi in this list")

list2 = [1,2,3,4,5]
if 3 in list2:
    print("There is 3 in this list")
