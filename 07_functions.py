
"""
Execute the below code in a cell by cell and see the output. There are Assignments to do it by your own, so complete that as well
Use Spyder to run and execute these .py files
"""


def function_name(parameters):
    statement(s)


def say_hi():
    print('Hi to Everyone')

def greet_everyone(greet):
    print(greet)

greet_everyone('Hello')



# Function Parameters

def add_number(X, Y):
    Z = X + Y
    print("Sum of {} + {} = {}".format(X, Y, Z))

X = 10
Y = 3
add_number(X, Y)



# Function Arguments

def simple_addition(num1,num2):
    answer = num1 + num2
    print('num1 is', num1)
    print(answer)
    
simple_addition(5,3)

# Keyword Arguments

simple_addition(num2=3,num1=5)


# Functions Parameters Defaults


def add_number(X, Y=10):
    Z = X + Y
    print("Sum of {} + {} = {}".format(X, Y, Z))


X = 10
add_number(X)

X = 10
add_number(X, Y=5)


color = ["red", "black"]
model = ["sports", "luxury"]


def car(color, model, brand="Ferrari"):
    for c in color:
        print("color :", c)
        if c == "red":
            model1 = model[0]
            print(brand, c, model1)
        else:
            print(brand, color[1], model[1])
    print("Selecting the car")


# arbitrary arguments - *args

def add_number(*nums):
    z = nums[0] + nums[1]
    print(z)

add_number(1, 2, 3,)

# arbitrary arguments - **kwargs

def add_number(**nums):
    z = nums['num1'] + nums['num2']
    print(z)

add_number(num1 = 1, num2 = 2, num = 3)



# Return Statement

def sum_num(arg1, arg2):
    total = arg1 + arg2
    return total

sum_num(10, 20)

total = sum_num(10, 20)
print(total)







