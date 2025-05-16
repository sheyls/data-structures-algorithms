# Given a 3x3 matrix, find the minimum cost to convert it into a magic square.
# A magic square is a 3x3 matrix where the sum of each row, column, and diagonal is equal to a number.
# The cost is the sum of the absolute differences between the original and the new matrix.

# The important thing is: there is a finite and small number of possible magic squares
# and always sum to 15.

from itertools import permutations

def formingMagicSquare(s):
    flat = [s[i][j] for i in range(3) for j in range(3)]
    best = float("inf")
    
    for perm in permutations(range(1,10)):
        #check rows
        if perm[0] + perm[1] + perm[2] != 15: 
            continue
        if perm[3] + perm[4] + perm[5] != 15: 
            continue
        if perm[6] + perm[7] + perm[8] != 15: 
            continue
        
        #check columns
        if perm[0] + perm[3] + perm[6] != 15: 
            continue
        if perm[1] + perm[4] + perm[7] != 15: 
            continue
        if perm[2] + perm[5] + perm[8] != 15: 
            continue
        
        #check diagonals
        if perm[0] + perm[4] + perm[8] != 15: 
            continue
        if perm[2] + perm[4] + perm[6] != 15: 
            continue
        
        cost = sum(abs(flat[i] - perm[i]) for i in range(9))
        
        if cost < best:
            best = cost
            
    return best

# Time complexity: O(9!) x O(1) = O(1)
# Space complexity: O(1)

# Test cases
print(formingMagicSquare([[4, 9, 2], [3, 5, 7], [8, 1, 5]])) # 1
