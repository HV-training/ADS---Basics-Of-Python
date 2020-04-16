
"""
Execute the below code in a cell by cell and see the output. There are Assignments to do it by your own, so complete that as well
Use the Spyder run and execute these .py files
"""

try:
    x = int(input("please enter a number: "))
except Exception as e:
    print(e)



def division_error():
    z = 10/0
    return z
try:
   division_error()
except ZeroDivisionError as err:
    print("Handling run-time error:", err)

# raise

x = 10
if x > 5:
    raise ValueError('x should not exceed 5. The value of x was: {}'.format(x))

# else clause

try:
    x = int(input("please enter a number: "))
except Exception as e:
    print(e)
else:
    print("No Exceptions caught")



# finally clause

try:
    x = int(input("please enter a number: "))
except Exception as e:
    print(e)
else:
    print("No Exceptions caught")
finally:
    print("The code block is closed")






# User defined Exceptions

# Index Error

l1 = [1, 2, 3]
l1[3]

# No module named
import nomodule

# Key Error
D1 = {'a': 1, 'b':2, 'c':3}
D1['4']

# cannot import name
from math import data



