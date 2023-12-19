'''
Given the root of a binary search tree and a target value,
return the value in the BST that is closest to the target.
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#work in progress
def closest_binary_search_tree(root, target):
    if not root:
        return None
    def dfs(node: TreeNode):
        if not node:
            return

        if abs(node.value - target) == 1:
            return node

        if target < node.value:
            dfs(node.left)
        elif target > node.value:
            dfs(node.right)


node_1 = TreeNode(1)
node_3 = TreeNode(3)
node_2 = TreeNode(2, node_1, node_3)
node_5 = TreeNode(5)
node_4 = TreeNode(4, node_2, node_5)
print(closest_binary_search_tree(node_4, 3.714286))