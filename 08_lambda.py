
"""
Execute the below code in a cell by cell and see the output. There are Assignments to do it by your own, so complete that as well
Use Spyder to run and execute these .py files
"""

def sum_num(arg1, arg2):
    return lambda total : arg1 + arg2

sum_num(2, 3)

lambda_func1 = (lambda x: x + 2)(2)
lambda_func2 = (lambda x,y: x + y)(2,3)
lambda_func3 = (lambda x,y,z : x+y*z) (2, 3, 4)




# map

def sum_num(x):
    return x + 1
total = list(map(sum_num, [1, 2, 3, 4, 5]))
print(total)


total = list(map(lambda x: x+1, [1, 2, 3, 4, 5]))
print(total)


# Reduce

from functools import reduce
reduce_func = reduce((lambda x, y: x+y),[2, 3, 4, 5])
reduce_func = reduce((lambda x, y: x*y),[2, 3, 4, 5])
reduce_func = reduce((lambda x, y: x%y),[2, 3, 4, 5])
print(reduce_func)

# filter

filter_func = list(filter(lambda x: x > 3, [1, 2, 4, 6, 7, 4, 9]))
filter_func = list(filter(lambda x: x % 2 == 0, [1, 2, 4, 6, 7, 4, 9]))

print(list(filter_func))


filter_list = list(filter(lambda x: (x<5), [1, 2, 3, 7, 8] ))
print("The filtered lists are", filter_list)

filtered_list2 = list(filter(lambda x: (x%2==0), [1, 2, 3, 7, 8]))
print(filtered_list2)

map_list = list(map(lambda x, y, z: x*y*z, [1, 2, 3], [4, 5, 6], [7, 8, 9]))
print(map_list)

reduce_list = reduce(lambda x, y: x * y, [1, 2, 3, 5, 6, 7])
print(reduce_list)


