# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
# T(n) and space complexity = O(n)

class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        global count
        count = 0

        def dfs(node):
            global count
            if not node.left and node.right:
                count += 1
                return True

            is_unival = True

            if node.left:
                is_unival = dfs(node.left) and node.left.val == node.val

            if node.right:
                is_unival = dfs(node.right) and node.right.val == node.val and is_unival

            if is_unival:
                count += 1
            return is_unival

        dfs(root)
        return count

def count_unival_subtrees_again(root:TreeNode) -> int:
    if not root:
        return 0
    global result

    result = 0
    def is_unival_sub_tree(node):
        global result
        # base case: if leaf node, then it's a unival
        if not node.left and not node.right:
            result += 1
            return True

        is_unival = True
        if node.left:
            is_unival = is_unival_sub_tree(node.left) and node.left.val == node.val
        if node.right:
            is_unival = is_unival_sub_tree(node.right) and is_unival and node.right.val == node.val

        if is_unival:
            result += 1
        return is_unival
    is_unival_sub_tree(root)
    return result

def test_count_unival_subtree():
    # node_level2_left = TreeNode(5)
    # node_level2_mid = TreeNode(5)
    # node_level2_right = TreeNode(5)
    # node_1 = TreeNode(1, node_level2_left, node_level2_mid)
    # node_level1_5 = TreeNode(5, right=node_level2_right)
    # node_level0_5 = TreeNode(5, node_1, node_level1_5)
    # print(count_unival_subtrees_again(node_level0_5) == 4)

    node_5_level2_left = TreeNode(5)
    node_5_level2_mid = TreeNode(5)
    node_5_level2_right = TreeNode(5)
    node_5_level1_left = TreeNode(5, node_5_level2_left, node_5_level2_mid)
    node_5_level1_right = TreeNode(5, None, node_5_level2_right)
    node_5_level0_left = TreeNode(5, node_5_level1_left, node_5_level1_right)
    print(count_unival_subtrees_again(node_5_level0_left) == 6)

