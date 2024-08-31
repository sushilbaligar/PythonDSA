# Type Error checking and conversion
print(type("abc")) #will give you <class 'str'>
print(type(123)) #will give you <class 'int'>
print(type(123.0)) #will give you <class 'float'>
print(type(True)) #will give you <class 'bool'>
print(type([])) #will give you <class 'list'>
print(type({})) #will give you <class 'dict'>
print(type(())) #will give you <class 'tuple'>
print(type(None)) #will give you <class 'NoneType'>
print(type(object)) #will give you <class 'type'>
print(type(__name__)) #will give you <class 'str'>
print(type(type)) #will give you <class 'type'>

#print("Number of letters in your name: " + str(len(input("Enter your name"))))

# PEMDAS
# Parentheses, Exponents, Multiplication/Division, Addition/Subtraction
print(3 * 3 + 3 / 3 - 3) # 7.0
print(3 * (3 + 3) / 3 - 3) # 3.0

# Number Manipulation and F-Strings in Python
int(3.738492) # Becomes 3
round(3.738492) # Becomes 4
round(3.14159) # Becomes 3
round(3.14159, 2) # Becomes 3.14
# In Python, we can use f-strings to insert a variable or an expression into a string.
age = 12
print(f"I am {age} years old")

import random
print(random.randint(1, 10)) # random numbers 1-10
print(random.random()) # random number between 0 and 1 - float
print(random.random() * 5) # random number between 0 and 5 float
print(random.uniform(1, 10)) # random number between 1 and 10 float

# how to get a random item from a List in Python.
list = [1, 2, 3, 4, 5]

