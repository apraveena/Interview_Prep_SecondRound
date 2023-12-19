"""
For your reference:
"""
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_a_bst(values):
    """
    Args:
     values(list_int32)
    Returns:
     BinaryTreeNode_int32
    """
    def insert(root: BinaryTreeNode, value):
        new_node = BinaryTreeNode(value)
        curr_node = root
        prev = None
        while curr_node is not None:
            if value == curr_node.value:
                print("KEY ALREADY EXISTS")
            elif value < curr_node.value:
                prev = curr_node
                curr_node = curr_node.left
            else:
                prev = curr_node
                curr_node = curr_node.right

        if value < prev.value:
            prev.left = new_node
        else:
            prev.right = new_node

        return root

    root = BinaryTreeNode(values[0])
    for i in range(1, len(values)):
        root = insert(root, values[i])

    return root
