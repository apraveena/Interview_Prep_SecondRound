"""
For your reference:
"""
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def lca(root, a, b):
    """
    Args:
     root(BinaryTreeNode_int32)
     a(BinaryTreeNode_int32)
     b(BinaryTreeNode_int32)
    Returns:
     int32
    """
    if a is b:
        return a.value
    LCA = [None]

    # Returns 2 flags indicating whether a and b are found in the subtree or not
    def dfs(node, a, b):
        afound, bfound = False, False

        if node is a:
            afound = True
        elif node is b:
            bfound = True

        if not node.left and not node.right:
            return afound, bfound

        if node.left:
            a_fnd, b_fnd = dfs(node.left, a, b)
            afound = afound or a_fnd
            bfound = bfound or b_fnd

        if node.right:
            a_fnd, b_fnd = dfs(node.right, a, b)
            afound = afound or a_fnd
            bfound = bfound or b_fnd

        if afound and bfound and LCA[0] is None:
            LCA[0] = node.value
            return True, True

        return afound, bfound

    dfs(root, a, b)
    return LCA[0]

node_2 = BinaryTreeNode(2)
node_1 = BinaryTreeNode(1)
node_1.left = node_2

print(lca(node_1, node_1, node_1))
