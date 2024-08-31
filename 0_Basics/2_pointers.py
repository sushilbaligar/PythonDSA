num1 = 11
num2 = num1
print("before num2 is updated >>>>> ")
print("num1=",num1, "points to:",id(num1))
print("num2=",num2, "points to:",id(num2))

num2 = 22 # creates new integer
print("\nAfter num2 is updated >>>>> ")
print("num1=", num1, "points to:", id(num1))
print("num2=", num2, "points to:", id(num2))
# Integers are immutable

dict1 = {
    'value': 11
}
dict2 = dict1
print("\nbefore dict2 is updated >>>>> ")
print("dict1=", dict1, "points to:", id(dict1))
print("dict2=", dict2, "points to:", id(dict2))

dict2['value'] = 22 # updates the dict value
print("\nAfter dict2 is updated >>>>> ")
print("dict1=", dict1, "points to:", id(dict1))
print("dict2=", dict2, "points to:", id(dict2))
# Dictionaries are mutable, so the pointers are the same


