# Write a Python function that takes a list of integers as input and returns a tuple containing the maximum and minimum values in the list.
def find_max_min(mylist):
    max = min = mylist[0]
    for num in mylist:
        if num > max:
            max = num
        if num < min:
            min = num
    return (max,min)

print( find_max_min([5, 3, 8, 1, 6, 9]) )
"""
    EXPECTED OUTPUT:
    ----------------
    (9, 1)
"""