# Given an integer array nums where the elements are sorted in ascending order, convert it to a
# height-balanced
#  binary search tree.
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#Time complexity and space complexity = O(n)
from typing import List, Optional

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        def helper(start, end):
            if start > end:
                return None

            if start == end:
                return TreeNode(nums[start])

            mid = start + (end - start) // 2
            root = TreeNode(nums[mid], left=helper(start, mid - 1), right=helper(mid + 1, end))
            return root

        return helper(0, len(nums) - 1)

def sorted_array_to_bst_again(arr: List[int]) -> Optional[TreeNode]:

    def helper(start, end):
        if start > end:
            return None

        if start == end:
            return TreeNode(arr[start])

        mid = start + (end - start)//2
        root = TreeNode(arr[mid], helper(start, mid-1), helper(mid+1, end))
        return root

    return helper(0, len(arr)-1)
