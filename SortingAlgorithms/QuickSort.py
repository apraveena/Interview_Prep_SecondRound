#Lomuto's partitioning
import random
def helper_Lomuto(arr, start, end):
    if start >= end:
        return
    pivot = random.randint(start, end)
    a[start], a[pivot] = a[pivot], a[start]

    smaller = start
    for bigger in range(start+1, end + 1):
        if a[bigger] < a[start]:
            smaller += 1
            a[smaller], a[bigger] = a[bigger], a[smaller]

    a[smaller], a[start] = a[start], a[smaller]
    helper(arr, start, smaller-1)
    helper(arr, smaller+1, end)

#Hoare's partitioning
def quick_sort_Lomuto(arr):
    helper(arr, 0, len(arr) -1)
    return arr

def helper(a, start, end):
    if start >= end:
        return
    small = start + 1
    big = end
    pivot = a[start]
    while big >= small:
        if a[small] <= pivot:
            small += 1
        elif a[big] > pivot:
            big -= 1
        else:
            a[small], a[big] = a[big], a[small]
            small += 1
            big -= 1
    a[big], a[start] = a[start], a[big]
    helper(a, start, big-1)
    helper(a, big + 1, end)


def quick_sort(arr):
    helper(arr, 0, len(arr)-1)
    return arr

a = [3, 5, 6, 8, 2, 7, 1]
a = [4, 2, 1, 3, 8, 7, 5, 6]
a = [6, 3, 6, 2, 2, 5, 7, 5, 9, 2]
print(a)
print(quick_sort(a))

# def quick_sort_trial_again(nums, l, r):
#     pivot, p = r, l
#     for i in range(r - l + 1):
#         if nums[i] <= pivot:
#             nums[i], nums[p] = nums[p], nums[i]
#             p += 1
#         else:


