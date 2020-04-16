
"""
Execute the below code in a cell by cell and see the output. There are Assignments to do it by your own, so complete that as well
Use the Spyder run and execute these .py files
"""


# While loop

number = 1
while number < 4:
    print(number)
    number += 1


# infnite loops

#number = 1
#while number < 10:
#     print(number)


# while else loops

number = 1
while number < 5:
    print(number)
    number += 1
else:
    print("count is not lessthan 5")



# For loop

exampleList = [1,5,6,6,2]

for x in exampleList:
    print(x)
    



fruit_basket = {"Apple": "Red", "Orange": "Orange", "Banana": "Yellow"}

for key, value in fruit_basket.items( ):
    print(key, value)
    




# Range
    
for x in range(1,3):
    print(x)

# enumerate
    
Days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
for indices, day in enumerate(Days):
    print(indices, day)


# Break

for number in range(4):
    number += 1
    print(number)
    break

# Continue
    
number = 0

for number in range(4):
    if number == 2:
        continue
    print('Number is ' + str(number))

print('Out of loop')


## Nested For loop

for x in range(1, 3):
    for y in range(1, 3):
        print ('%d * %d = %d' % (x, y, x*y))



# Assignment - 2

"""        
Write a program to iterate on each word in a sentence, 
print word along with index for each iteration
"""

sample_text = "A watched pot never boils" 

# Your Code Here










        
        
        
