"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""


def get_maximum_value(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     int32
    """
    if root is None:
        return None
    curr = root
    while curr.right is not None:
        curr = curr.right

    return curr.value

