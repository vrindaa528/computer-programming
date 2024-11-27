#Convert to ASCII Values
#Question: Write a program to convert each character in a string to its ASCII value.

#Solution:

s = "hello"
ascii_values = [ord(char) for char in s]
print(ascii_values)  # Output: [104, 101, 108, 108, 111]
