# Tuples are used to store multiple items in a single variable
mytuple = ("apple", "banana", "cherry") # A tuple is a collection which is ordered and unchangeable.
print(mytuple)

# ordered
# unchangeable
# allow duplicates
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

# Tuple Length
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

# Create Tuple With One Item

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple") # str
print(type(thistuple))

# Tuple Items - Data Types 

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

print(tuple1)
print(tuple2)
print(tuple3)

# can combine

tuple1 = ("abc", 34, True, 40, "male")

print(tuple1)

# type
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

# The tuple() Constructor
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

