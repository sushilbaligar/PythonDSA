# Implement a Python function called print_items.
def print_items_n(n):
    for i in range(n): 
        print(i)
    
print_items_n(10)  
# Time complexity: O(n) as it runs n times
# Space complexity: O(1) as it uses constant space regardless of input size

def print_items_2n(n):
    for i in range(n): 
        print(n)
    for j in range(n): 
        print(n) 

print_items_2n(10)
# Time complexity: O(2n). Drop constant. So, its O(n).
# Space complexity: O(1) as it uses constant space regardless of input size

def print_items_nsq(n):
    for i in range(n): 
        for j in range(n): 
            print(i, j)

print_items_nsq(10)
# Time complexity: O(n^2) as it runs n^2 times
# Space complexity: O(1) as it uses constant space regardless of input size

def print_items_nsqn(n):
    for i in range(n): 
        for j in range(n): 
            print(i, j)
    for i in range(n): 
        print(n)
print_items_nsqn(10)
# Time complexity: O(n^2+n). Drop non-dominant term n. Hence its O(n^2).
# Space complexity: O(1) as it uses constant space regardless of input size





