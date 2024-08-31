counter = 0
# Without Memoization time comp is O(2^n) - Incredibly Inefficient
def fib(n):
    global counter
    counter += 1
    if n == 0 or n == 1:
        return n
    return fib(n-1) + fib(n-2)

print(fib(20))
print(counter) # returns 22k fn calls
print("******************************************")

#**************************************************
# With Memoization time comp is O(n) - Efficient
counter = 0
fib_cache = {}
def fib_memo(n):
    global counter
    counter += 1
    global fib_cache
    if n in fib_cache:
        return fib_cache[n]
    if n == 0 or n == 1:
        return n
    fib_cache[n] = fib_memo(n-1) + fib_memo(n-2)
    return fib_cache[n]

print(fib_memo(20))
print(counter) # return 2*n-1 (hence O(n)) 39 fn calls

print("******************************************")
# Fibonacci with bottom-up approach
counter = 0
def fib_bottom_up(n):
    fib_list = [0,1]
    global counter
    for i in range(2,n+1):
        counter += 1
        next_fib = fib_list[i-1] + fib_list[i-2]
        fib_list.append(next_fib)
    return fib_list[n]

print(fib_bottom_up(20))
print(counter) # return n-1 (hence O(n)) 19 fn calls 

    