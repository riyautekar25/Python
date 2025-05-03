# Enums have names and values associated with them. 
'''
Enumerations or Enums is a set of symbolic names bound to unique values. It can be iterated over to return its canonical members in definition order. It provides a way to create more readable and self-documenting code by using meaningful names instead of arbitrary values.
'''
# name - value pair
from enum import Enum
class Months(Enum):
    JAN = 1
    FEB = 2
    MAR = 3
    APR = 4

for month in Months:
    print(month.name ,"-", month.value)

print(Months(4).name)
print(Months['APR'].value)
print(type(Months))