# Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.
# Interleaving means that s3 contains all the characters of s1 and s2 and the order of the characters can be different
# but the characters of s1 and s2 are in the same order as they were in s1 and s2.

#Sol 1
def is_interleave(s1: str, s2: str, s3: str) -> bool:
    if len(s3) != len(s1) + len(s2):
        return False
    
    if not s3:
        return not s1 and not s2
 
    if s1 and s3[0] == s1[0]:
        if is_interleave(s1[1:], s2, s3[1:]):
            return True

    if s2 and s3[0] == s2[0]:
        if is_interleave(s1, s2[1:], s3[1:]):
            return True

    return False

#O(2^n+m)

#Sol 2 (Memoization)

def is_interleave_memo(s1: str, s2: str, s3: str) -> bool:
    if len(s3) != len(s1) + len(s2):
        return False
     
    memo = {}
    def helper(i, j):
        k = i + j

        if i == len(s1) and j == len(s2):
            return True
        
        if (i,j) in memo:
            return memo[(i,j)]
        
        if i < len(s1) and s1[i] == s3[k] and helper(i+1, j):
                memo[(i,j)] = True
                return True
        
        if j < len(s2) and s2[j] == s3[k] and helper(i, j+1):
                memo[(i,j)] = True
                return True
        
        memo[(i,j)] = False
        return False
    
    return helper(0,0)

#O(NxM)

#Sol 3 (DP)

def is_interleave_dp(s1: str, s2: str, s3: str) -> bool:
    if len(s3) != len(s1) + len(s2):
        return False
    
    dp = [[False] * (len(s2)+1) for _ in range(len(s1)+1)]
    dp[-1][-1] = True

    for i in range(len(s1), -1, -1):
        for j in range(len(s2), -1, -1):
            if i < len(s1) and s1[i] == s3[i+j] and dp[i+1][j]:
                    dp[i][j] = True

            if j < len(s2) and s2[j] == s3[i+j] and dp[i][j+1]:
                    dp[i][j] = True

    return dp[0][0]

# O(NxM)


s1 = "aa"
s2 = "ab"
s3 = "aaba"

print(is_interleave_dp(s1, s2, s3))  # Debería imprimir True
