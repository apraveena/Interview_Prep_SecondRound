from collections import deque
"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
def postorder(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     list_int32
    """
    result = []
    def dfs(root):
        if root is None:
            return
        if root.left:
            dfs(root.left)
        if root.right:
            dfs(root.right)
        result.append(root.value)
    dfs(root)
    return result


"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""

def postorder_traversal_iterative(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     list_int32
    """
    post_order = []
    if not root:
        return post_order
    stack = deque()
    stack.append(root)

    while stack:
        curr_node = stack[-1]
        if curr_node.left:
            stack.append(curr_node.left)
            curr_node.left = None
        elif curr_node.right:
            stack.append(curr_node.right)
            curr_node.right = None
        else:
            post_order.append(curr_node.value)
            stack.pop()

    return post_order






