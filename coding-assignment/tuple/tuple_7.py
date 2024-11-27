#Zip Multiple Tuples
#Question: Write a program to zip multiple tuples together.

#Solution:

tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')
tuple3 = (True, False, True)
zipped = tuple(zip(tuple1, tuple2, tuple3))
print(zipped)  # Output: ((1, 'a', True), (2, 'b', False), (3, 'c', True))
