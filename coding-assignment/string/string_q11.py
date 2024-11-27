#Longest Palindromic Substring
#Question: Write a program to find the longest palindromic substring in a given string.

#Solution:

def longest_palindromic_substring(s):
    n = len(s)
    if n == 0:
        return ""
    result = ""
    for i in range(n):
        for j in range(i, n):
            substr = s[i:j+1]
            if substr == substr[::-1] and len(substr) > len(result):
                result = substr
    return result

s = "babad"
print(longest_palindromic_substring(s))  # Output: "bab" or "aba"
