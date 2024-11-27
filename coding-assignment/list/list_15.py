#Split List into Chunks
#Question: Write a program to split a list into chunks of a specified size.

#Solution:


my_list = [1, 2, 3, 4, 5, 6, 7, 8]
chunk_size = 3
chunks = [my_list[i:i + chunk_size] for i in range(0, len(my_list), chunk_size)]
print(chunks)  # Output: [[1, 2, 3], [4, 5, 6], [7, 8]]
