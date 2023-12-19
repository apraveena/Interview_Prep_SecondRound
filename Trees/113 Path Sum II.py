# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
from typing import Optional, List


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        slate = []
        if root is None:
            return []
        def dfs(node, slate):
            if not node.left and not node.right:
                if sum(slate) == targetSum:
                    result.append(slate[:])
                return

            if node.left:
                slate.append(node.left.val)
                dfs(node.left, slate)
                slate.pop()

            if node.right:
                slate.append(node.right.val)
                dfs(node.right, slate)
                slate.pop()

        slate.append(root.val)
        dfs(root, slate)
        return result

node_7, node_2, node_5_leaf, node_1 = TreeNode(7), TreeNode(2), TreeNode(5), TreeNode(1)
node_11 = TreeNode(11, node_7, node_2)
node_13 = TreeNode(13)
node_4_level_2 = TreeNode(4, node_5_leaf, node_1)
node_8 = TreeNode(8, node_13, node_4_level_2)
node_4 = TreeNode(4, node_11)
node_5 = TreeNode(5, node_4, node_8)

sln = Solution()
print(sln.pathSum(node_5, 22))

