from typing import List

#it's ok to use auxiliary space
def square_of_sorted_arr(a):
    n = len(a)
    left = 0
    right = n - 1
    result = [0] * n
    for i in range(n-1, -1, -1):
        if abs(a[left]) > abs(a[right]):
            sq = a[left]
            left += 1
        else:
            sq = a[right]
            right -= 1
        result[i] = sq ** 2
    return result

#Tried doing the sort with O(1) space complexity - didn't work
def sq_of_sorted_arr(a):
    left = 0
    right = len(a)-1

    while right >= left:
        if abs(a[left]) >= abs(a[right]):
            a[left], a[right] = a[right], a[left]
            a[right] = a[right] * a[right]
            right -= 1
        else:
            a[left] = a[left] * a[left]
            left += 1
    return a

#From leetcode
def sortedSquares(nums: List[int]) -> List[int]:
    n = len(nums)
    result = [0] * n
    left = 0
    right = n - 1
    for i in range(n - 1, -1, -1):
        if abs(nums[left]) < abs(nums[right]):
            square = nums[right]
            right -= 1
        else:
            square = nums[left]
            left += 1
        result[i] = square * square
    return result

lst1 = [-9, -4, -1, 2, 1, 4, 8]
lst1 =  [-9, -5, -2, 0, 3, 7]
lst1 =  [-9, -5, 0, 3]
print(lst1)
print(square_of_sorted_arr(lst1))