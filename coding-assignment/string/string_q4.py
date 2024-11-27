#Remove Duplicates
#Question: Write a program to remove duplicate characters from a string.

#Solution:

s = "hello"
unique_chars = "".join(sorted(set(s), key=s.index))
print(unique_chars)  # Output: "helo"
