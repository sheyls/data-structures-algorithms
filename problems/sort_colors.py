# Given an array of length N containing only 0s, 1s, and 2s, sort the array in ascending order.

# Sol 1
def sort_array(array: list):
    repetitions = [0, 0, 0]
    for i in array:
        repetitions[i] += 1
    result = []
    for i, j in enumerate(repetitions):
        result.extend([i] * j)
    print(result)

array = [2,0,2,1,1,0]
sort_array(array)

# O(N) time
# O(N) space

# Sol 2
def sort_array_pointers(array: list):
    l, r = 0, len(array) - 1
    i = 0

    while i <= r:
        if array[i] == 0:
            array[l], array[i] = array[i], array[l]
            l += 1
        elif array[i] == 2:
            array[r], array[i] = array[i], array[r]
            r -= 1
            i -= 1
        i += 1

    return array

# O(N) time
# O(1) space

array = [2, 1, 1, 0, 0, 2]
print(sort_array_pointers(array))
