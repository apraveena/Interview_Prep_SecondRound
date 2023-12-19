#From Dave from ik
import random

def radix_sort(arr):
    max_val = max(arr)
    exp = 1
    while max_val//exp > 0:
        count_sort(arr, exp)
        exp = 10
    return arr

def count_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    for i in range(n):
        index = (arr[i]//exp) % 10
        count[index] += 1
    for i in range(1,10):
        count[i] += count[i-1]
    i = n-1
    while i>=0:
        index = (arr[i]//exp) % 10
        output[count[index]-1] = arr[i]
        count[index] -= 1
        i -= 1
    i = 0
    for i in range(n):
        arr[i] = output[i]


a = [0] * 100
for i in range(len(a)):
    a[i] = random.randrange(1,101)

print(radix_sort([8, 3, 6, 2, 2]))