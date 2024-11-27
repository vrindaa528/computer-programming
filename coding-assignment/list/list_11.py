#Count Frequency of Elements
#Question: Write a program to count the frequency of each element in a list.

#Solution:

my_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
frequency = {}
for item in my_list:
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1
print(frequency)  # Output: {1: 1, 2: 2, 3: 3, 4: 4}
