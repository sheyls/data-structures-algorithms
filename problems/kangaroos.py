def kangaroo(x1, v1, x2, v2):
    if v1 == v2:
        return "YES" if x1 == x2 else "NO"
    if x2 > x1 and v2 > v1: 
        return "NO"
    elif x1 > x2 and v1 > v2 :
        return "NO"
        
    if (x2 - x1) % (v1 - v2) == 0:
        if x2 != x1: return "YES"
        
    return "NO"

# Time complexity: O(1)
# Space complexity: O(1)
        
print(kangaroo(0, 3, 4, 2))  # Output: YES