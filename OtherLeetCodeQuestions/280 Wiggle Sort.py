from typing import List

class Solution:
    def wiggleSort1(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) in (0, 1):
            return nums

        left, right = 0, 1
        n = len(nums)
        check_left = True
        while left <= right and right <= n :
            original_right = right
            if check_left:
                if right < n and nums[left] > nums[right]:
                    while right < n - 1 and nums[left] > nums[right]:
                        needs_swap = True
                        right += 1
                    if original_right == right:
                        nums[left], nums[right] = nums[right], nums[left]
                    else:
                        nums[left + 1], nums[right] = nums[right], nums[left + 1]
                    right = left + 1
                else:
                    right += 1
            else:
                if right < n and nums[left] < nums[right]:
                    while right < n - 1 and nums[left] < nums[right]:
                        right += 1

                    if original_right == right:
                        nums[left], nums[right] = nums[right], nums[left]
                    else:
                        nums[left + 1], nums[right] = nums[right], nums[left + 1]
                    right = left + 1
                else:
                    right += 1

            left += 1

            check_left = not check_left
        return nums

    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) in (0, 1):
            return nums

        left, right = 0, 1
        n = len(nums)
        check_left = True
        while left <= right and right <= n :
            if check_left:
                if right < n and nums[left] > nums[right]:
                    nums[left], nums[right] = nums[right], nums[left]
            else:
                if right < n and nums[left] < nums[right]:
                    nums[left], nums[right] = nums[right], nums[left]

            left += 1
            right += 1

            check_left = not check_left
        return nums

sln = Solution()

lst1 = [2, 1]
print(f"List: {lst1}, expected output: [1, 2]")
print(sln.wiggleSort(lst1))

print()

lst1 = [3, 5, 2, 1, 6, 4]
print(f"List: {lst1}, expected output: [3, 5, 1, 6, 2, 4] or [1, 6, 2, 5, 3, 4] or [3, 5, 2, 6, 1, 4]")
print(sln.wiggleSort(lst1))

print()

lst2 = [6,6,5,6,3,8]
print(f"List: {lst2}, expected output: [6,6,5,6,3,8]")
print(sln.wiggleSort(lst2))

print()

lst2 = [6, 7, 8, 2, 1, 5, 4]
print(f"List: {lst2}, expected output: [6,7, 2, 8, 1, 5, 4]")
print(sln.wiggleSort(lst2))