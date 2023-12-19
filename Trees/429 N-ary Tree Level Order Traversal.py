#Leetcde 429
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from typing import List
import collections
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []

        result = []
        queue = collections.deque()
        queue.append(root)
        while queue:
            temp = []
            for i in range(len(queue)):
                curr = queue.popleft()
                temp.append(curr.val)
                for child in curr.children:
                    queue.append(child)
            result.append(temp[:])
        return result