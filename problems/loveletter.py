# Loveletter problem (Hackerrank)
# Given a string s, you may only decrement letters (e.g. ‘d’→‘c’) toward ‘a’, one step per operation.
# Compute the minimum number of such operations needed to turn s into a palindrome.


def theLoveLetterMystery(s):

    if len(s) < 2:
        return 0
    
    r = len(s) - 1
    l = 0
    
    def reduce(big, lit):
        count = 0
        while big > lit:
            big -= 1
            count += 1
        return count
    
    total_count = 0
    
    while r > l:
        lc = ord(s[l])
        rc = ord(s[r])

        if lc > rc:
            total_count += reduce(lc, rc)
        elif lc < rc:
            total_count += reduce(rc, lc)
        
        r -= 1
        l += 1
                   
    return total_count
        
# Time complexity: O(n)
# Space complexity: O(1)

# Test cases
print(theLoveLetterMystery("abc")) # 2
print(theLoveLetterMystery("abcba")) # 0
print(theLoveLetterMystery("abcd")) # 4
print(theLoveLetterMystery("cba")) # 2
