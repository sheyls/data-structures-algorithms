def merge_sort(array):

    if len(array) <= 1:
        return array
    
    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    return merge(left, right)

def merge(left, right):
    sol = []
    l = r = 0
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            sol.append(left[l])
            l += 1
        elif left[l] > right[r]:
            sol.append(right[r])
            r += 1

    sol.extend(left[l:])
    sol.extend(right[r:])
    return sol

# O(NlogN)

lista = [64, 34, 25, 12, 22, 11, 90]
print("Merge Sort:", merge_sort(lista.copy()))