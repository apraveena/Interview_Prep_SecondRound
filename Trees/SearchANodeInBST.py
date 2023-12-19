"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""


def search_node_in_bst(root, value):
    """
    Args:
     root(BinaryTreeNode_int32)
     value(int32)
    Returns:
     bool
    """
    if root is None:
        return False

    curr_node = root
    while curr_node is not None:
        if curr_node.value == value:
            return True
        elif value > curr_node.value:
            curr_node = curr_node.right
        else:
            curr_node = curr_node.left

    return False

