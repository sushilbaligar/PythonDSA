# Creating a set
fruits = {"apple", "banana", "cherry"} # using curly braces
fs = set(["cherry"]) # using set constructor
print(type(fruits))
print(len(fruits))
print(fruits)
print(fs)

# Adding elements
fruits.add("orange")
print(fruits)

# Removing elements
fruits.remove("banana")
# fruits.remove("banana") KeyError as element is not present in set 
fruits.discard("banana") # no error if element not present in set
print(fruits)

# Checking membership
print("apple" in fruits)  # Output: True

# Set operations
other_fruits = {"kiwi", "cherry", "grape"}
print(fruits.union(other_fruits))  # Merge both
print(fruits.intersection(other_fruits))  # print common item
print(fruits.difference(other_fruits))  # diff items in fruits
print(fruits.symmetric_difference(other_fruits))  #diff items in both sets
print(fs.issubset(other_fruits))
print(other_fruits.issuperset(fs))
fs2 = set(["mango"])  
print(fs2.isdisjoint(other_fruits)) # no commons items present?  
print(fruits.copy())  # Output: {'orange', 'apple', 'cherry'}
print(fruits.clear())  # Output: None
print(fruits)  # Output: set() empty set as clear removed elements

# How can you remove duplicates from a list using a set?
my_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = list(set(my_list))
print(unique_list)  # Output: [1, 2, 3, 4, 5] (order may vary)

# How can you find common elements between two lists using sets?
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
common_elements = set(list1).intersection(set(list2))
print(common_elements)  # Output: {3, 4}