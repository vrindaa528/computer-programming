#Remove Punctuation
#Question: Write a program to remove all punctuation from a string.

#Solution:

import string

s = "hello, world!"
no_punctuation = s.translate(str.maketrans("", "", string.punctuation))
print(no_punctuation)  # Output: "hello world"
