"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""


def height_of_binary_tree(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     int32
    """
    if not root: return 0

    global max_ht
    max_ht = 0

    def helper(node):
        global max_ht
        my_max_ht, left_ht, right_ht = 1, 0, 0

        if node.left:
            left_ht = helper(node.left) + 1
            my_max_ht = max(left_ht, my_max_ht)

        if node.right:
            right_ht = helper(node.right) + 1
            my_max_ht = max(right_ht, my_max_ht)

        max_ht = max(max_ht, my_max_ht)
        return my_max_ht

    helper(root)
    return max_ht
