#Check Prime
#Question: Write a function to check if a number is prime.

#Solution:

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Example
result = is_prime(7)
print(result)  # Output: True
