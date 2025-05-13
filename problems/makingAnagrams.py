# Given two strings s1 and s2 that may not be of the same length, 
# determine the minimum number of character deletions required to make  and  anagrams. 
# Any characters can be deleted from either of the strings.

from collections import defaultdict

def makingAnagrams(s1, s2):
    dic = defaultdict(int)
    for s in s1:
        dic[s] += 1
    
    for s in s2:
        dic[s] -= 1
    
    result = sum(abs(v) for v in dic.values())
    
    return result

# Time complexity: O(n)
# Space complexity: O(k)

def makingAnagrams2(s1, s2):
    
    count = [0]*26
    
    for s in s1:
        count[ord(s) - 97] += 1
    
    for s in s2:
        count[ord(s) - 97] -= 1

    result = sum(abs(v) for v in count)
    
    return result

# Time complexity: O(n)
# Space complexity: O(1)

# Test cases
print(makingAnagrams("abc", "cde")) # 4