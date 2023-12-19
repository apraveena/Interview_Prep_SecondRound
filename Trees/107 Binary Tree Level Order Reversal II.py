# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional
from collections import deque


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        queue = deque()
        result = []
        queue.append(root)
        while queue:
            temp = []
            for _ in range(len(queue)):
                curr = queue.popleft()
                temp.append(curr.val)
                if curr.left: queue.append(curr.left)
                if curr.right: queue.append(curr.right)

            result.append(temp[:])

        result.reverse()
        return result
