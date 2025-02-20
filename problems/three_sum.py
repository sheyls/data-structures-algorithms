# Three Sum: Given a array of integers, are there elements a, b, c in the array such that a + b + c = 0? 
# Find all unique triplets in the array which gives the sum of zero.

from typing import List

def three_sum(array: List[int]):
    sol = []
    array.sort()

    for i,a in enumerate(array):
        if i > 0 and a == array[i-1]:
            continue

        l,r = i+1, len(array)-1
        while l < r:
            sum = a + array[l] + array[r]
            if sum > 0:
                r -= 1
            elif sum < 0:
                l += 1
            else:
                sol.append([a, array[l], array[r]])
                l += 1 
                while array[l] == array[l-1] and l < r: 
                    l += 1 
        return sol

# O(n^2)