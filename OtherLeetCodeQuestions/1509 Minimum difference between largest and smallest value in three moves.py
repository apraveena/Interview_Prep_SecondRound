'''If the size <= 4, then just delete all the elements and either no or one element would be left giving the answer 0.
else sort the array
there are 4 possibilities now:-

delete 3 elements from left and none from right
delete 2 elements from left and one from right
delete 1 from left and 2 from right
delete all three elements from the right
now just print the minimum value

From my understanding, deleting as in ignoring the value
'''
from typing import List

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4: return 0
        nums.sort()
        return min(nums[-1] - nums[3], nums[-2] - nums[2], nums[-3] - nums[1], nums[-4] - nums[0])