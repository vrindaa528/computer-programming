#Sum of Digits
#Question: Write a function to find the sum of digits of a number.

#Solution:

def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

# Example
result = sum_of_digits(123)
print(result)  # Output: 6
