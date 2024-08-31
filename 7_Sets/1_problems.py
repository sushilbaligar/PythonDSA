# has unique chars
def has_unique_chars(string):
    if string == "":
        return True
    char_set = set(string)
    return len(char_set) == len(string)

def has_unique_chars(string):
    if string == "":
        return True
    char_set = set()
    for char in string:
        if char in char_set:
            return False
        char_set.add(char)
    return True

print(has_unique_chars('abcdefg')) # should return True
print(has_unique_chars('hello')) # should return False
print(has_unique_chars('')) # should return True
print(has_unique_chars('0123456789')) # should return True
print(has_unique_chars('abacadaeaf')) # should return False

# Find pairs
def find_pairs(arr1, arr2, target):
    my_pairs = []
    if len(arr1) == 0 or len(arr2) == 0:
        return my_pairs
    my_set = set(arr1)
    for item in arr2:
        complement = target - item
        if complement in  my_set:
            my_pairs.append((item, complement)) 
    return my_pairs

arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 4, 6, 8, 10]
target = 7

pairs = find_pairs(arr1, arr2, target)
print (pairs)

# Set: Longest consecutive sequence
def longest_consecutive_sequence(nums):
    num_set = set(nums)
    max_length = 0
    for num in nums:
        if num - 1 not in num_set:
            current_num = num
            current_length = 1
            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1
            max_length = max(max_length, current_length)
    return max_length