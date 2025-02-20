def bubble_sort(array):
    n = len(array) - 1
    for i in range(n):
        for j in range(n-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

# O(N^2)

lista = [64, 34, 25, 12, 22, 11, 90]
print("Bubble Sort:", bubble_sort(lista.copy()))