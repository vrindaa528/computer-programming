#Find GCD
#Question: Write a function to find the greatest common divisor (GCD) of two numbers.

#Solution:

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Example
result = gcd(48, 18)
print(result)  # Output: 6
