# Longest Palindrome Substring: Given a string, find the longest substring which is palindrome.

def longest_palindrome(s: str) -> str:
    result = ""
    len_result = 0

    n = len(s)

    def palindrom(l,r):
        nonlocal result, len_result
        while l >= 0 and r < n and s[l] == s[r]:
            if (r - l + 1) > len_result:
                result = s[l:r+1]
                len_result = r - l + 1
            l -= 1
            r += 1

    for i in range(n):
        palindrom(i,i+1)
        palindrom(i,i)

    return result
    
# O(N^2)

s = "babad"
print(longest_palindrome(s)) #"bab" or "aba"