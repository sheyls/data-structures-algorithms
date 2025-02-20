# Search a number in a 2D matrix. The matrix is sorted in a way that the first integer of each row is greater than the last integer of the previous row.
# Example: [[1, 3, 5], [7, 9, 11], [13, 15, 17]], search 7, return True.
# Example: [[1, 3, 5], [7, 9, 11], [13, 15, 17]], search 14, return False.

from typing import List


def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    ROWS, COLUMNS = len(matrix), len(matrix[0])

    top, bot = 0, ROWS - 1

    while top <= bot:
        mid = (top + bot) // 2

        if target > matrix[mid][-1]:
            top = mid + 1
        elif target < matrix[mid][0]:
            bot = mid - 1
        else:
            break
    
    if top > bot:
        return False
    
    row = (top + bot) // 2

    left, right = 0, COLUMNS - 1

    while left <= right:
        mid = (left + right) // 2

        if target > matrix[row][mid]:
            left = mid + 1
        elif target < matrix[row][mid]:
            right = mid - 1
        else:
            return True
    
    return False

# O(log(MxN))    

matrix = [[1, 3, 5], [7, 9, 11], [13, 15, 17]]
target = 14

print(searchMatrix(matrix, target))