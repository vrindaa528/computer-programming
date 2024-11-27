#Fibonacci Sequence
#Question: Write a function to return the nth Fibonacci number.

#Solution:

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Example
result = fibonacci(6)
print(result)  #output:8
