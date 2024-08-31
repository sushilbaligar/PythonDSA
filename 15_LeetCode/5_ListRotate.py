# List: Rotate ( ** Interview Question)
# You are given a list of n integers and a non-negative integer k.
# Your task is to write a function called rotate that takes the list of integers and an integer k as input and rotates the list to the right by k steps.
def rotate(nums, k):
    k = k % len(nums)
    nums[:] = nums[-k:] + nums[:-k]

nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
rotate(nums, k)
print("Rotated array:", nums)
"""
    EXPECTED OUTPUT:
    ----------------
    Rotated array: [5, 6, 7, 1, 2, 3, 4]
"""