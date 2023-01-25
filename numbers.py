# There is 3 different types
# int
a = 1
e = 1212345678878
f = -121232
# float
b = 2.4
g = 2.0
h = -123.321
i = 12e2
j = 21E12
k = -34.2e21

# complex
c = 1j
l = 2+3j
m = 4j
n = -21j

# getting the data type
print(type(a))
print(type(e))
print(type(f))
print(type(b))
print(type(g))
print(type(h))
print(type(i))
print(type(j))
print(type(k))
print(type(c))
print(type(l))
print(type(m))
print(type(n))

# converting

x = 1
y = 1.0
z = 1j

# int to float
a = float(x)
print(a)
print(type(a))

# float to int
b = int(y)
print(b)
print(type(b))

# int to complex
c = complex(x)
print(c)
print(type(c))

# cannot convert complex into other number
d = int(z)

