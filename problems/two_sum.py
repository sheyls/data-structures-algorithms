#Two Sum: Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.

from typing import List

def two_sum(array: List[int], target: int) -> tuple:
    past_values = {}
    for i, j in enumerate(array):
        dif = target - j
        if dif in past_values:
            return (past_values[dif], i)
        past_values[j] = i

array = [2, 7, 11, 15]
target = 9

print(two_sum(array, target)) #(0, 1)
# O(N)

