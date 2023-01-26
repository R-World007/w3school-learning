# True or False
# any expression in python |operators and operands
# compare two value
# can answer True or False

# Example
print(1==1)
print(123==321)
print(0<1)

# can print a message or something based on whether the condition is False or True

a = int(input("A? "))
b = int(input("B? "))

if b > a:
    print("B is greater than A")
else:
    print("B is not greater than A")

# bool()  function allows you to evaluate any value or variables, and give you True or False in return,

# Evaluate Values
print(bool("Hello"))
print(bool(14))

# Evaluate Variable

x = 1234
y = "Sai"
print(bool(x))
print(bool(y))

# Most Values are True But
# Any string is True, except empty strings
# Any numbeer is True, except 0
# Any list, tuple, set, and dictionary are True, except empty ones

# Examples of True

bool("abc..z")
bool(123)
bool([2,3,4])

# Example of False

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))


class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

# Function can Return a Boolean

def myfunction():
    return True
print(myfunction())
if myfunction():
    print("Yes")
else:
    print("No")

# isinstance() | build-in Function

f = 200
print(isinstance(f, int))

