# Given a string s say yes if can be rearranged to form a palindrome, otherwise no.

from collections import defaultdict

def gameOfThrones(s):
    dic = defaultdict(int)
    for c in s:
        dic[c] += 1

    odd = sum( v % 2 for v in dic.values() )

    resp = "YES" if odd <= 2 else "NO"
    
    return resp

# Test cases
print(gameOfThrones("aaabbb")) # YES
print(gameOfThrones("cdefghmnopqrstuvw")) # NO