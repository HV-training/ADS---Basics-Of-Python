
"""
Execute the below code in a cell by cell and see the output. There are Assignments to do it by your own, so complete that as well
Use Spyder to run and execute these .py files
"""


x = [1,3,5,6,2,1,6]
print(type(x))


# list methods

x = [1,6,3,2,4,1,2,6,7]

x.append(55) # 
x.insert(2,43) # insert based on index
x.extend([2, 3, 4])
x.remove(3) # remove the fist occurance element
x.pop(10) # remove based on index and return the value
x.reverse() # reverse the order in list
x.sort() # sorting by default ascending
x.sort(reverse = True) # sorting in descending




# Accesing Values in the List

x = [10, 15, 16, 17]
x[1]
x[2]


# Slicing

x = [1,3,5,6,2,1,6]
print(type(x))

x[1:4]
x[-4:-1]
x[:3]
x[::2]
x[::-1]

## Multi Dimensional List

fruits = [["Apple", "Red"], ["Orange", "Orange"], ["Banana", "Yellow"], ["Grape", "Black"]]
fruits[0]
fruits[0][1]
fruits[0][1] = "Green" # update list
del fruits[0][1] # delete based on index

print(fruits)











