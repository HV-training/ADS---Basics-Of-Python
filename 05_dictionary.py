
"""
Execute the below code in a cell by cell and see the output. There are Assignments to do it by your own, so complete that as well
Use Spyder to run and execute these .py files
"""

fruit_basket = {"Apple": "Red", "Orange": "Orange", "Banana": "Yellow"}
fruit_basket['Apple']
fruit_basket['Orange']
fruit_basket["strawberry"] = "Red" # adding new element
del fruit_basket["strawberry"] # deleting on key


# Accesing Values from Dictionary


fruits = {"Apple": ["Red", "round"], "Orange": ["Orange", "round"], "Banana": ["Yellow", "hook"]}
fruits["Apple"][0]
fruits["Orange"][0]


# Accesing all the keys and values

fruits.keys()
fruits.values()

for k in fruits:
    print(k, fruits[k])



# Multi dimensional Dictionary

fruits = {"fruits_name":{
    "Apple":{
        "color":"red",
        "Shape": "round"
        
    },
    
    "Orange":{
        "color":"Orange",
        "Shape": "round"
    }
}}

fruits["fruits_name"]
fruits["fruits_name"]["Apple"]


## python Dictionary Comprehension

squares = {x: x**x for x in range(1,10)}
even_numbers = {x: x**x for x in range(1,10) if x%2==0}




