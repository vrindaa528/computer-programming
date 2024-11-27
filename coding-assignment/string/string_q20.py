#Wildcard Matching
#Question: Implement wildcard pattern matching with support for '?' and ''. The '?' matches any single character, and the '' matches any sequence of characters (including the empty sequence).

#Solution:

def is_match(s, p):
    s_len, p_len = len(s), len(p)
    dp = [[False] * (p_len + 1) for _ in range(s_len + 1)]
    dp[0][0] = True

    for j in range(1, p_len + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]

    for i in range(1, s_len + 1):
        for j in range(1, p_len + 1):
            if p[j - 1] == '*':
                dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
            elif p[j - 1] == '?' or s[i - 1] == p[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]

    return dp[s_len][p_len]

s = "aa"
p = "*"
print(is_match(s, p))  # Output: True
