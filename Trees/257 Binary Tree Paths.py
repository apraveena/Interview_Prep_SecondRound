# Definition for a binary tree node.
from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        result = []
        if root is None:
            return [""]

        def helper(node, slate):
            if (not node.left) and (not node.right):
                result.append("->".join(slate))
                return

            if node.left:
                slate.append(str(node.left.val))
                helper(node.left, slate)
                slate.pop()

            if node.right:
                slate.append(str(node.right.val))
                helper(node.right, slate)
                slate.pop()

        helper(root, [str(root.val)])
        return result

sln = Solution()
node_5 = TreeNode(5)
node_2 = TreeNode(2, None, node_5)
node_3 = TreeNode(3)
node_1 = TreeNode(1, node_2, node_3)

print(sln.binaryTreePaths(node_1))