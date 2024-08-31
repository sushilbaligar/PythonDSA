# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)

# Creating a tuple with mixed data types
mixed_tuple = (1, "hello", 3.14, True)

# Creating a tuple with a single element (note the comma)
single_element_tuple = (1,)

# Creating an empty tuple
empty_tuple = ()

print(my_tuple)          # Output: (1, 2, 3, 4, 5)
print(mixed_tuple)       # Output: (1, 'hello', 3.14, True)
print(single_element_tuple)  # Output: (1,)
print(empty_tuple)       # Output: ()

# Accessing elements
first_element = my_tuple[0]
last_element = my_tuple[-1]

print(first_element)   # Output: 1
print(last_element)    # Output: 5

# Slicing tuples
subset = my_tuple[1:4]  # Output: (2, 3, 4)
print(subset)
reversed_tuple = my_tuple[::-1]  # Output: (5, 4, 3, 2, 1)
print(reversed_tuple)

# Unpacking tuples
a, b, c, d, e = my_tuple
print(a, b, c, d, e)  # Output: 1 2 3 4 5

# Attempting to modify a tuple
try:
    my_tuple[0] = 10
except TypeError as e:
    print(e)  # Output: 'tuple' object does not support item assignment

# Tuples have only two built-in methods:
# count(): Counts occurrences of a value.
# index(): Finds the index of the first occurrence of a value.
example_tuple = (1, 2, 3, 4, 5)
print(example_tuple.count(2))  # Output: 1
print(example_tuple.index(5))  # Output: 4

#You can convert a list to a tuple using the tuple() constructor:
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print(my_tuple)  # Output: (1, 2, 3)

# How do you handle unpacking of tuples when the number of elements is not fixed?
# You can use the "extended unpacking" feature introduced in Python 3. If you don’t know the number of elements in advance, you can use the * operator to capture multiple elements:
a, *rest, b = (1, 2, 3, 4, 5)
print(a)     # Output: 1
print(rest)  # Output: [2, 3, 4]
print(b)     # Output: 5

# What are some common use cases for tuples in Python?
# Returning Multiple Values: Functions can return multiple values as a tuple.
# Fixed Collections: Tuples are used to group related pieces of data that should not be changed.
# Dictionary Keys: Tuples can be used as keys in dictionaries because they are immutable and hashable.
# Unpacking: Tuples are used in unpacking assignments for extracting multiple values from iterables.