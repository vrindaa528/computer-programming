#Find Factorial
#Question: Write a function to find the factorial of a number.

#Solution:


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Example
result = factorial(5)
print(result)  # Output: 120
