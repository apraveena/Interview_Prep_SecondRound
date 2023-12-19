"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""


def flip_upside_down(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     BinaryTreeNode_int32
    """
    if not root:
        return root
    if not root.left and not root.right:
        return root

    new_root = flip_upside_down(root.left)
    root.left.left = root.right
    root.left.right = root
    root.left = None
    root.right = None
    return new_root




class BinaryTreeNode:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right




def print_Binary_Tree(root):
    result = []
    def dfs(node):
        if node.left: dfs(node.left)
        result.append(node.value)
        if node.right: dfs(node.right)
    dfs(root)
    return result

# node_2 = BinaryTreeNode(2)
# node_3 = BinaryTreeNode(3)
# node_1 = BinaryTreeNode(1, node_2, node_3)
# print(print_Binary_Tree(node_1))
# res = flip_upside_down(node_1)
# print(print_Binary_Tree(res))

node_6 = BinaryTreeNode(6)
node_7 = BinaryTreeNode(7)
node_4 = BinaryTreeNode(4, node_6, node_7)
node_5 = BinaryTreeNode(5)
node_2 = BinaryTreeNode(2, node_4, node_5)
node_3 = BinaryTreeNode(3)
node_1 = BinaryTreeNode(1, node_2, node_3)
print(print_Binary_Tree(node_1))
res = flip_upside_down(node_1)
print(print_Binary_Tree(res))



