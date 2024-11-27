#Count Vowels
#Question: Write a function to count the number of vowels in a string.

#Solution:


def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = sum(1 for char in s if char in vowels)
    return count

# Example
result = count_vowels("hello")
print(result)  # Output: 2
