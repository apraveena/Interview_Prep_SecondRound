# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional
import collections
from math import inf

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return root
        q = collections.deque()
        q.append(root)
        max_sum, max_sum_level = -inf, 1
        curr_level = 0

        while q:
            curr_level = curr_level + 1
            curr_sum = 0
            for i in range(len(q)):
                curr_node = q.popleft()
                curr_sum += curr_node.val
                if curr_node.left:
                    q.append(curr_node.left)
                if curr_node.right:
                    q.append(curr_node.right)

            if curr_sum > max_sum:
                max_sum = curr_sum
                max_sum_level = curr_level

        return max_sum_level

