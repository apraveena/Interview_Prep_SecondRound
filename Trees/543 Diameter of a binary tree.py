# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

#Time and space complexityis O(n) space for call stack (worst case scenario)
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        global max_diameter
        if root is None:
            return 0
        max_diameter = 0
        def dfs(node):
            global max_diameter
            if not node.left and not node.right:
                return 0

            left_ht, right_ht = 0, 0
            if node.left:
                left_ht = dfs(node.left) + 1

            if node.right:
                right_ht = dfs(node.right) + 1

            max_diameter = max(max_diameter, left_ht + right_ht)
            return max(left_ht, right_ht)
        dfs(root)
        return max_diameter

node_4 = TreeNode(4)
node_5 = TreeNode(5)
node_2 = TreeNode(2, node_4, node_5)
node_3 = TreeNode(3)
node_1 = TreeNode(1, node_2, node_3)

sln = Solution()
print(sln.diameterOfBinaryTree(node_1)) # expected answer is 3

