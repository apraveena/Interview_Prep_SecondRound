from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        global sum_flag
        if not root:
            return False
        sum_flag = False

        def dfs(root, sub_sum):
            global sum_flag

            if (not root.left) and (not root.right):
                if sub_sum + root.val == targetSum:
                    sum_flag = True
                return

            if root.left:
                dfs(root.left, sub_sum + root.val)
                if sum_flag: return

            if root.right:
                dfs(root.right, sub_sum + root.val)
                if sum_flag: return


        dfs(root, 0)
        return sum_flag

    #better performant
    def hasPathSum_rewrite(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # Time: O(n) | Space: O(n)
        if not root:
            return False

        if not root.left and not root.right and root.val == targetSum:
            return True

        targetSum -= root.val

        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)

sln = Solution()

node_7, node_2, node_1 = TreeNode(7), TreeNode(2), TreeNode(1)
node_11, node_13, node_4_right = TreeNode(11, node_7, node_2), TreeNode(13), TreeNode(4, right =node_1)
node_4, node_8 = TreeNode(4, left=node_11), TreeNode(8, node_13, node_4_right)
root = TreeNode(5, node_4, node_8)
print(sln.hasPathSum(root, 22))

node_2, node_3 = TreeNode(2), TreeNode(3)
root = TreeNode(1, node_2, node_3)
print(sln.hasPathSum(root, 5))
