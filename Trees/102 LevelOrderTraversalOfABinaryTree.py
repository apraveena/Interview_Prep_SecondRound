#leetcode 102
"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
from collections import deque


def level_order_traversal(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     list_list_int32
    """
    if root is None:
        return []
    result = []
    queue = deque()
    queue.append(root)
    while queue:
        temp = []
        for i in range(len(queue)):
            curr = queue.popleft()
            temp.append(curr.value)
            if curr.left: queue.append(curr.left)
            if curr.right: queue.append(curr.right)
        result.append(temp[:])

    return result


