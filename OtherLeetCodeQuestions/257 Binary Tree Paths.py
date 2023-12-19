from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths_mytry(self, root: Optional[TreeNode]) -> List[str]:

        result = []
        if root is None:
            return []

        def helper(node, slate):
            if node == None:
                return
            else:
                if node.left is None and node.right is None:
                    slate.append(str(node.val))
                    result.append("->".join(slate))
                    return

            slate.append(str(node.val))
            if node.left: helper(node.left, slate, node)
            slate.pop()
            slate.append(str(node.val))
            if node.right: helper(node.right, slate, node)
            slate.pop()

        helper(root, "", None)
        return result

    #from leetcode solution
    def binaryTreePaths(self, root):
        res = []

        def dfs(node, s):
            if s != "":
                s += "->"
            s += str(node.val)
            if not node.left and not node.right: res.append(s)
            if node.left: dfs(node.left, s)
            if node.right: dfs(node.right, s)

        dfs(root, "")
        return res



# lst1 = [1,2,3,None,5]
right_2 = TreeNode(5)
left_1 = TreeNode(2, right = right_2)
right_1 = TreeNode(3)
tree_node = TreeNode(1, left_1, right_1)

sln = Solution()

print(sln.binaryTreePaths(tree_node))