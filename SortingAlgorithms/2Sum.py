#twosum
def indices_of_two_sum(a, target):
    hmap = {}
    for i in range(len(a)):
        n1 = a[i]
        n2 = target - n1
        if n2 in hmap:
            return [i, hmap[n2]]
        else:
            hmap[n1] = i
    return [-1, -1]

from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    result = [-1, -1]
    hmap = {}
    for i, num in enumerate(nums):
        target_sum = target - num
        if target_sum in hmap:
            result = [i, hmap[target_sum]]
        else:
            hmap[num] = i

    return result
lst = [2,7,11,15,8]
print(twoSum(lst, 19) == [4, 2] or twoSum(lst, 19) == [2, 4])