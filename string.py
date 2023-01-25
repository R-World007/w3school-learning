# ".." or '..'
print("Sai")
print('.H')

# assign the string to variable and multiline Strings

a = """ Sai.H is
good preson. Hello,
To all. """

print(a)

b = ''' Sai.H is
good preson. Hello,
To all. '''
print(b)

# strings are Arrays
# strings in python are arrays of bytes representing unicode characters.
# But in python there is no character data type, a single character is a length of q

# []can be used to access elements of the string

c = "Hello, World!"
print(c[1]) # 0 is the first character

# looping Through a string
for x in "apple":
    print(x)

# string length
print(len(c))

# check String (in)
d = "Love is power!"
print("Love" in d)

if "Love" in d:
    print("Yes, I agree!")

# check if not
e = 'The best things in life are free!'
print("expensive" not in e)
if "expensive" not in e:
    print("NO, 'expensive' is NOT present")

