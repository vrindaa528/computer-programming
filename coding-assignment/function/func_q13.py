#Find Median
#Question: Write a function to find the median of a list of numbers.

#Solution:


def find_median(lst):
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_lst[mid - 1] + sorted_lst[mid]) / 2
    else:
        return sorted_lst[mid]

# Example
result = find_median([3, 1, 4, 1, 5, 9])
print(result)  # Output: 3.5
