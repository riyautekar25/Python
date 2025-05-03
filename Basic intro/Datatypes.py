'''
Python is an interpreted language: meaning it is read line by line, without separate compilation step.
This means the interpreter reads the source code and translates it into machine-readable instructions on the fly, allowing the program to run immediately. 

Since everything is an object in Python programming, Python data types are classes and variables are instances (objects) of these classes. 
Numeric – int, float, complex
Sequence Type – string, list, tuple
Mapping Type – dict
Boolean – bool
Set Type – set, frozenset
Binary Types – bytes, bytearray, memoryview 
type operator can be used to get the data type of the object'''

#  int, float, string, list and set
x = 50
x = 60.5
x = "Hello World"
x = ["geeks", "for", "geeks"]
x = ("geeks", "for", "geeks")

# number data types
a = 5
print(type(a))

b = 5.0
print(type(b))

c = 2 + 4j
print(type(c))

# sequence data type: string list tuple
s = 'Welcome to the Geeks World'
print(s)

# check data type 
print(type(s))

# access string with index
print(s[1])
print(s[2])
print(s[-1])

# Empty list
l = []

# list with int values
l = [1, 2, 3]
print(l)

# list with mixed int and string
l2 = ["Geeks", "For", "Geeks", 4, 5]
print(l2)

# initiate empty tuple
tup1 = ()

tup2 = ('Geeks', 'For')
print("\nTuple with the use of String: ", tup2)

tup1 = tuple([1, 2, 3, 4, 5])

# access tuple items
print(tup1[0])
print(tup1[-1])
print(tup1[-3])

# Boolean data type
print(type(True))
print(type(False))
#print(type(true)) # error as Python is case sensitive

# set datatype in python
# initializing empty set
s1 = set()

s1 = set("GeeksForGeeks")
print("Set with the use of String: ", s1)

s2 = set(["Geeks", "For", "Geeks"])
print("Set with the use of List: ", s2)
print(type(s2))

set1 = set(["Geeks", "For", "Geeks"])
print(set1)

# loop through set
for i in set1:
    print(i, end="/")
print()
# check if item exist in set    
print("Geeks" in set1)

# dictionary in python
# initialize empty dictionary
d = {}

d = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print(d)

# creating dictionary using dict() constructor
d1 = dict({1: 'Geeks', 2: 'For', 3: 'Geeks'})
print(d1)
d = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}

# Accessing an element using key
print(d['name'])

# Accessing a element using get
print(d.get(3))