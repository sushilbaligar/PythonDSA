# Factorial function using recursion
# DEBUG THIS PROGRAM TO UNDERSTAND CALL STACK AND BASE CASE SCENARIO
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(4))