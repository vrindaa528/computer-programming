#Convert Decimal to Binary
#Question: Write a function to convert a decimal number to a binary number.

#Solution:


def decimal_to_binary(decimal):
    return bin(decimal).replace("0b", "")

# Example
result = decimal_to_binary(10)
print(result)  # Output: "1010"
