#Longest Common Prefix

#Question: Write a program to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string "".

#Solution:

def longest_common_prefix(strs):
    if not strs:
        return ""

    # Start with the first string as the initial prefix
    prefix = strs[0]

    for s in strs[1:]:
        while s[:len(prefix)] != prefix:
            prefix = prefix[:-1]
            if not prefix:
                return ""
    
    return prefix

# Example
strs = ["flower", "flow", "flight"]
print(longest_common_prefix(strs)) # Output: "fl"
