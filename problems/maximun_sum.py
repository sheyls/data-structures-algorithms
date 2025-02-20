#Maximun sum: Given an array of integers, find the contiguous subarray with the largest sum.

# Sol 1
def maximun_sum(array):
    max_sum = float("-inf")
    n = len(array)
    for i in range(n):
        sum = 0
        for j in range(i,n):
            sum += array[j]
            max_sum = max(max_sum, sum)
    return max_sum

# O(N^2)

# Sol 2 (Kadane's Algorithm)
def maximun_sum_2(array):
    max_sum = array[0]
    sum = 0
    for n in array:
        if sum < 0:
            sum = 0
        sum += n
        max_sum = max(max_sum, sum)
    return max_sum

# O(N)

# Original Kadane's Algorithm

def maximun_sum_ka(array):
    max_sum = sum = array[0]
    for n in array[1:]:
        sum = max(n, sum+n)
        max_sum = max(max_sum, sum)
    return max_sum

array = [-2,1,-3,4,-1,2,1,-5,4]
print(maximun_sum_2(array)) #6