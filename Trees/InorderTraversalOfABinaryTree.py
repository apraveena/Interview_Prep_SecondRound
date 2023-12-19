"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
def inorder(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     list_int32
    """
    results = []
    if root is None:
        return results

    def dfs(node):
        if node.left is not None:
            dfs(node.left)
        results.append(node.value)
        if node.right is not None:
            dfs(node.right)

    dfs(root)
    return results


from typing import List, Optional
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal_iterative(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        in_order = []
        stack = deque()
        stack.append(root)
        while stack:
            curr_node = stack[-1]
            if curr_node.left:
                stack.append(curr_node.left)
                curr_node.left = None
            else:
                # first add my value then process right
                in_order.append(curr_node.val)
                right_node = curr_node.right
                stack.pop()
                if curr_node.right:
                    stack.append(right_node)
        return in_order



