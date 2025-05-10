# Gemstones
# Given a list of rocks represented as strings, find the number of gemstones.
# A gemstone is a mineral that appears in every rock.

def gemstones(arr):
    n = len(arr)
    alph = [0]*26
    
    for a in arr:
        seen = [False]*26
        for m in a:
            seen[ord(m)-97] = True
        for i in range(26):
            if seen[i]:
                alph[i] += 1
    gem = sum(1 for count in alph if count == n)

    return gem

# Time complexity: O(n)
# Space complexity: O(1)

# Test cases
print(gemstones(["abcdde", "baccd", "eeabg"])) # 2
print(gemstones(["a", "b", "c"])) # 0