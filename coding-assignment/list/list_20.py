#Common Divisors of List Elements
#Question: Write a program to find common divisors of all elements in a list.

#Solution:
from functools import reduce
import math

my_list = [24, 36, 60]
def gcd(a, b):
    return math.gcd(a, b)

common_divisors = reduce(gcd, my_list)
print(common_divisors)  # Output: 12
