#leetcode 103
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional, List
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        result = []
        flip = False
        queue = collections.deque()
        queue.append(root)
        while queue:
            temp = []
            for _ in range(len(queue)):
                curr = queue.popleft()
                temp.append(curr.val)
                if curr.left: queue.append(curr.left)
                if curr.right: queue.append(curr.right)
            if flip:
                temp.reverse()
            result.append(temp[:])
            flip = not flip
        return result


