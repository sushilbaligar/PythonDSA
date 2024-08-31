# Given a sorted list of integers, rearrange the list in-place such that all unique elements appear at the beginning of the list.
def remove_duplicates(my_list):
    if not my_list:
        return 0
    count = 0
    for i in range(1,len(my_list)):
        if my_list[i] != my_list[i-1]:
            count += 1
            my_list[count] = my_list[i]
    return count+1


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
new_length = remove_duplicates(nums)
print("New length:", new_length)
print("Unique values in list:", nums[:new_length])