'''
Given an array of integers of size ‘n’,
Our aim is to calculate the maximum sum of ‘k’ consecutive elements in the array

Input  : arr[] = {100, 200, 300, 400}, k = 2
Output : 700

Input  : arr[] = {1, 4, 2, 10, 23, 3, 1, 0, 20}, k = 4
Output : 39
We get maximum sum by adding subarray {4, 2, 10, 23} of size 4.

Input  : arr[] = {2, 3}, k = 3
Output : Invalid
There is no subarray of size 3 as size of whole array is 2.
'''
import sys

def max_sum_brute_force(arr, k):
    n = len(arr)
    if n < k:
        return -1
    max_sum = -sys.maxsize + 1
    for i in range(n - k + 1):
        temp_sum = 0
        for j in range(k):
            temp_sum += arr[i + j]

        max_sum = max(max_sum, temp_sum)
    return max_sum

def max_sum_sliding_window(arr, k):
    n = len(arr)
    if n < k:
        return -1
    curr_sum = max_sum = sum(arr[:k])

    for j in range(n - k ):
        curr_sum = curr_sum - arr[j] + arr[k + j]
        max_sum = max(max_sum, curr_sum)

    return max_sum

def test_max_sum_brute_force():
    print()
    print(max_sum_brute_force([100, 200, 300, 400], 2) == 700)
    print(max_sum_brute_force([1, 4, 2, 10, 23, 3, 1, 0, 20], 4) == 39)
    print(max_sum_brute_force([2, 3], 3) == -1)
    print(max_sum_sliding_window([100, 200, 300, 400], 2) == 700)
    print(max_sum_sliding_window([1, 4, 2, 10, 23, 3, 1, 0, 20], 4) == 39)
    print(max_sum_sliding_window([2, 3], 3) == -1)

print(max_sum_sliding_window([100, 200, 300, 400], 2) == 700)