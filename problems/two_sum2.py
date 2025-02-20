# Two sum 2: Given an array of integers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number.

from typing import List

def two_sum_2(array: List[int], target: int) -> tuple:

    pi, pf = 0, len(array)-1

    while pi < pf:
        sum = array[pi] + array[pf] 
        if sum > target:
            pf -= 1
        elif sum < target:
            pi += 1
        else:
            return (pi+1, pf+1)
    
    return(-1,-1)

  

array = [2, 7, 11, 15]
target = 9

print(two_sum_2(array, target)) #(1, 2)