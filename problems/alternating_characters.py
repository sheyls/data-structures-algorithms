# Problem: https://www.hackerrank.com/challenges/alternating-characters/problem
# Given a string s, delete the minimum number of characters from s to make it alternating.
# An alternating string is one where no two adjacent characters are the same.

def alternatingCharacters(s):
    deletions = 0
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            deletions += 1
    return deletions

# Time complexity: O(n)
# Space complexity: O(1)

# Test cases
print(alternatingCharacters("AAAA")) # 3
print(alternatingCharacters("BBBBB")) # 4
print(alternatingCharacters("ABABABAB")) # 0
print(alternatingCharacters("BABABA")) # 0
print(alternatingCharacters("AAABBB")) # 4
