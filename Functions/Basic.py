'''
Python def keyword is used to define a function
'''
#Passing Function as an Argument
# *args : when we are passing multiple arguments to a function
def foo(fo,*arg):
    return fo(*arg)

def mul(*nums):
    flag=1
    for num in nums:
        flag=flag*num
    return flag
ans = foo(mul,5,2,3)
print(ans)

# **kwargs: used as an argument for collecting key-value pairs into a dictionary
def func2(**kwargs):
    for key,value in kwargs.items():
        print(key,value)
func2(name="Raji",age=33)

# return statement
# if you use return statement for returning multiple values then it gets return in form of tuple

# local variable and global variable 
'''
local variable: accessible inside a function
global variable: accessible throughout program
unless and until u spcify global keyword inside the function the varible is by default local in that function
'''

#recursion: function calling itslef directly or indirectly
def factorial(num):
    if num==0:
        return 1
    else:
        return num*factorial(num-1)
print(factorial(5))

'''
# just try :)
def sum(num):
    sum=0
    while num>0:
        rem=num%10
        sum+=rem
        num=num//10
    return sum
print(sum(321))
'''
# try recursion: stack concept
def rec2(num):
    if num>0:
        result=num+rec2(num-1)
        print(result)
    else:
        result=0
    return result
print(rec2(6))


"""
Python inner functions: nested functions, nonlocal keyword allows the nested function to use local variable of host fucntion and also allows it to modify the variable unlike global keyword
inner function allows encapsulation
"""

"""
help() gives documentation of any fucntion in python. use: print(func_name.__doc__) ---> to print docstring of any fucntion.
"""