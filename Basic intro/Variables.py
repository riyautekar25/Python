'''
Variables act as placeholders for data. They allow us to store and reuse values in our program.
Variables in Python are assigned values using the = operator.
'''
# Python variables are dynamically typed, meaning the same variable can hold different types of values during execution.
x = 10
x = "Now a string"

# Python allows multiple variables to be assigned values in a single line.
a = b = c = 100
print(a, b, c)
#We can assign different values to multiple variables simultaneously
x, y, z = 1, 2.5, "Python"
print(x, y, z)

# Typecasting: refers to the process of converting the value of one data type into another. 
# Implicit and explicit type casting

# implicit type Casting 
# Python automatically converts 
# a to int 
a = 7
print(type(a)) 

# Python automatically converts 
# b to float 
b = 3.0
print(type(b)) 

# Python automatically converts 
# c to float as it is a float addition 
c = a + b 
print(c) 
print(type(c))

# Python automatically converts 
# d to float as it is a float multiplication
d = a * b
print(d)
print(type(d))


# Python program to demonstrate explicit type Casting : using int(), float(), str()

# int variable
a = 5

# typecast to float
n = float(a)

print(n)
print(type(n))