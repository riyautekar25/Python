'''
if, if-else, shorthand if else (ternary operator), elif, nested-if, match-case statement (in python 10)
'''
number = 2

match number:
    case 1:
        print("One")
    case 2 | 3:
        print("Two or Three")
    case _:
        print("Other number")

'''
for, while, nested, do while

loop control statements: continue, pass, break
'''

# How for loop works internally?
fruits = ["apple", "mango", "kiwi"]
for fruit in fruits:
    print(fruit)
# iter() and next() method **it requires StopIteration
iter_obj = iter(fruits)
while True:
    try:
        fruit = next(iter_obj)
        print(fruit)
    except StopIteration:
        break