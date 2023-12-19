'''
Given 2 arrays and target sum, count the number of sub arrays that add up to target sum
both arrays must be used
Interview question from capital one.. trying solution here
'''
def target_sum_2_arrays(arr1, arr2, target):
    global count
    if len(arr1) == 0 or len(arr2) == 0:
        return 0
    smaller_array = arr1 if len(arr1) > len(arr2) else arr2
    bigger_array = arr2 if len(arr1) <= len(arr2) else arr1
    count = 0

    def is_intersection(arr1, arr2):
        return len([value for value in arr1 if value in arr2]) > 0

    def combinations(slate, arr):
        global count

        if len(arr) == 0:
            return

        if sum(slate) == target and is_intersection(arr1, slate) and is_intersection(arr2, slate) :
            count += 1

        slate.append(arr[0])
        combinations(slate, arr[1:])
        slate.pop()

    combinations([], smaller_array + bigger_array)

    return count

arr1 = [1, 2, 4, 6, 7, 3, 5]
arr2 = [2, 1, 5, 7, 4, 3]
target = 20

arr1 = [5, 3, 2, 1]
arr2 = [2, 5, 3]
target = 10

# print(target_sum_2_arrays(arr1, arr2, target))

from collections import defaultdict

def target_sum_ways(arr1, arr2, target_sum):
    freq1 = defaultdict(int)
    freq2 = defaultdict(int)

    for num in arr1:
        freq1[num] += 1

    for num in arr2:
        freq2[num] += 1

    count = 0

    for num1 in freq1:
        num2 = target_sum - num1
        if num2 in freq2:
            count += freq1[num1] * freq2[num2]

    return count

arr1 = [1, 2, 3, 5, 1]
arr2 = [2, 5, 1, 1]
target_sum = 5
#Expected answer: 4
# values from arr1                  values from arr2
# 1, 1                              3
# 3                                 2
# 2                                 1, 2
# 1, 3                              1
print(target_sum_ways(arr1, arr2, target_sum))


