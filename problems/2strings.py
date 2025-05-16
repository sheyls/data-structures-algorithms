# Given two strings, determine if they share a common substring. A substring may be as small as one character.
def twoStrings(s1, s2):
    alpha = [0]*26
    for s in s1:
        alpha[ord(s) - 97] += 1
    
    for s in s2:
        if alpha[ord(s) - 97] >= 1:
            return "YES"
    
    return "NO" 