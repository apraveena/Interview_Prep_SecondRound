#wasn't working.. check again
def bubble_sort(nums):
    size = len(nums)
    for k in range(size - 1):
        swapped = False
        for l in range(size - k - 1):
            if nums[l] > nums[l + 1]:
                swapped = True
                nums[l], nums[l + 1] = nums[l + 1], nums[l]
        if swapped == False: break

    return nums

print(bubble_sort([4, 5, 6, 9, 2]))
print(bubble_sort([1, 4, 5, 6, 9, 2]))
print(bubble_sort([1, 2, 2, 4, 5, 6]))
print(bubble_sort([6, 5, 4, 3, 2, 1]))
print(bubble_sort([6, 4, 4, 1, 2, 3]))
