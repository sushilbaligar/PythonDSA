# Find item in common in two lists
# O(n) time complexity
# O(n) space complexity
def item_in_common(list1, list2):
    my_dict = {}
    for i in list1:
        my_dict[i] = True

    for j in list2:
        if j in my_dict:
            return True
    return False

list1 = [1, 3, 5]
list2 = [2, 4, 5]
list3 = [2, 4, 6]
print("****** Item in Common ********")
print(item_in_common(list1, list2))
print(item_in_common(list1, list3))

# Find duplicates in an array
# O(n) time complexity
# O(n) space complexity
def find_duplicates(arr):
    my_dict = {}
    duplicates = []
    for num in arr:
        if num in my_dict:
            if num not in duplicates:
                duplicates.append(num)
        else:
            my_dict[num] = 1
    return duplicates
print("****** Duplicates in an Array ********")
print ( find_duplicates([1, 2, 3, 4, 5]) )
print ( find_duplicates([1, 1, 2, 2, 3]) )
print ( find_duplicates([1, 1, 1, 1, 1]) )
print ( find_duplicates([1, 2, 3, 3, 3, 4, 4, 5]) )
print ( find_duplicates([1, 1, 2, 2, 2, 3, 3, 3, 3]) )
print ( find_duplicates([1, 1, 1, 2, 2, 2, 3, 3, 3, 3]) )
print ( find_duplicates([]) )

# Find first non repeating character in a string
# O(n) time complexity
# O(n) space complexity
def first_non_repeating_char(string):
    my_dict = {}
    for char in string:
        if char in my_dict:
            my_dict[char] += 1
        else:
            my_dict[char] = 1

    for char in string:
        if my_dict[char] == 1:
            return char
    return None

print("****** First Non Repeating Character in a String ********")
print(first_non_repeating_char('programming'))
print(first_non_repeating_char('hello'))
print(first_non_repeating_char(''))

# Group anagrams together
# O(n * k * log k) time complexity
# O(n * k) space complexity
def group_anagrams(strings):
    my_dict = {}
    for string in strings:
        sorted_string = ''.join(sorted(string))
        if sorted_string in my_dict:
            my_dict[sorted_string].append(string)
        else:
            my_dict[sorted_string] = [string]
    return list(my_dict.values())
print("****** Group Anagrams ********")
print("1st set:")
print( group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) )

print("\n2nd set:")
print( group_anagrams(["abc", "cba", "bac", "foo", "bar"]) )

print("\n3rd set:")
print( group_anagrams(["listen", "silent", "triangle", "integral", "garden", "ranged"]) )

# Two Sum 
# O(n) time complexity
# O(n) space complexity
def two_sum(nums, target):
    my_dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in my_dict:
            return [my_dict[complement], i]
        my_dict[num] = i
    return []
print("****** Two Sum ********")    
print(two_sum([5, 1, 7, 2, 9, 3], 10))  
print(two_sum([4, 2, 11, 7, 6, 3], 9))  
print(two_sum([10, 15, 5, 2, 8, 1, 7], 12))  
print(two_sum([1, 3, 5, 7, 9], 10))  
print ( two_sum([1, 2, 3, 4, 5], 10) )
print ( two_sum([1, 2, 3, 4, 5], 7) )
print ( two_sum([1, 2, 3, 4, 5], 3) )
print ( two_sum([], 0) )

# subarray sum
# O(n) time complexity
# O(n) space complexity
def subarray_sum(nums, target):
    my_dict = {0: -1}
    current_sum = 0
    for i, num in enumerate(nums):
        current_sum += num
        if current_sum - target in my_dict:
            return [my_dict[current_sum - target] + 1, i]
        my_dict[current_sum] = i
    return []
print("****** Subarray Sum ********")
nums = [1, 2, 3, 4, 5]
target = 9
print ( subarray_sum(nums, target) )

nums = [-1, 2, 3, -4, 5]
target = 0
print ( subarray_sum(nums, target) )

nums = [2, 3, 4, 5, 6]
target = 3
print ( subarray_sum(nums, target) )

nums = []
target = 0
print ( subarray_sum(nums, target) )

def subarraysum(nums,target):
    my_dict = {}
    current_sum = 0
    for i, num in enumerate(nums):
        current_sum += num
        if current_sum - target in my_dict:
            return [my_dict[current_sum - target] + 1, i]
        my_dict[current_sum] = i
    return []