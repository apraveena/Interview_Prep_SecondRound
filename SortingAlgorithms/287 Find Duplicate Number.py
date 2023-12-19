#My solution in Kaya interview - no extra space, no modifying the array

class Solution:
    from typing import List
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] in nums[:i] + nums[i+1:]:
                return nums[i]

        return -1