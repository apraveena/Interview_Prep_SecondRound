# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional
import collections
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional
from collections import deque

class Solution:
    #temp is an integer
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        queue = collections.deque()
        queue.append(root)
        result = []
        while queue:
            temp = 0
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr.left: queue.append(curr.left)
                if curr.right: queue.append(curr.right)
                temp = curr.val

            result.append(temp)
        return result
    #with temp as list - other solution is preferred
    def rightSideView_temp_as_list(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        queue = collections.deque()
        queue.append(root)
        result = []
        while queue:
            temp = []
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr.left: queue.append(curr.left)
                if curr.right: queue.append(curr.right)
                temp.append(curr.val)

            result.append(temp[-1])
        return result

