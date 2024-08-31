# List: Max Sub Array ( ** Interview Question)
# Given an array of integers nums, write a function max_subarray(nums) that finds the contiguous subarray (containing at least one number) with the largest sum and returns its sum.
def max_subarray(nums):
    max_sum = nums[0]  # Initialize max_sum with the first element
    current_sum = nums[0]  # Initialize current_sum with the first element
    for num in nums[1:]:
        # Update current_sum to be the maximum of the current element or
        # the sum of the current element and the previous current_sum
        current_sum = max(num, current_sum + num)
        # Update max_sum to be the maximum of max_sum and current_sum
        max_sum = max(max_sum, current_sum)
    return max_sum

# Example 1: Simple case with positive and negative numbers
input_case_1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result_1 = max_subarray(input_case_1)
print("Example 1: Input:", input_case_1, "\nResult:", result_1)  
# Example 2: Case with a negative number in the middle
input_case_2 = [1, 2, 3, -4, 5, 6]
result_2 = max_subarray(input_case_2)
print("Example 2: Input:", input_case_2, "\nResult:", result_2) 
# Example 3: Case with all negative numbers
input_case_3 = [-1, -2, -3, -4, -5]
result_3 = max_subarray(input_case_3)
print("Example 3: Input:", input_case_3, "\nResult:", result_3) 
"""
    EXPECTED OUTPUT:
    ----------------
    Example 1: Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4] 
    Result: 6
    Example 2: Input: [1, 2, 3, -4, 5, 6] 
    Result: 13
    Example 3: Input: [-1, -2, -3, -4, -5] 
    Result: -1
    
"""