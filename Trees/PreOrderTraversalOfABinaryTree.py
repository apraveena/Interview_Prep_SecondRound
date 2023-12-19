"""
For your reference:
"""
class BinaryTreeNode:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

def preorder(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     list_int32
    """
    result = []
    if not root: return result
    
    def dfs(node: BinaryTreeNode):
        result.append(node.value)
        if node.left: dfs(node.left)
        if node.right: dfs(node.right)

    dfs(root)
    return result

node_3 = BinaryTreeNode(3)
node_4 = BinaryTreeNode(4)
node_1 = BinaryTreeNode(1, node_3, node_4)
node_2 = BinaryTreeNode(2)
root = BinaryTreeNode(0, node_1, node_2)
print(preorder(root))

from typing import List, Optional
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal_iterative(self, root: Optional[TreeNode]) -> List[int]:
        #iterative
        if not root:
            return []
        preorder = []
        stack = deque()
        stack.append([root, False])
        while stack:
            curr_node, is_visited = stack[-1]
            if not is_visited:
                preorder.append(curr_node.val)
                stack[-1][1] = True #Set the visited var to True to avoid adding it multiple times

            if curr_node.left:
                stack.append([curr_node.left, False])
                curr_node.left = None
            elif curr_node.right:
                stack.append([curr_node.right, False])
                curr_node.right = None
            else:
                stack.pop()
        return preorder
