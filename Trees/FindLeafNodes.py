"""
For your reference:
"""
class BinaryTreeNode:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

def find_leaves(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     list_list_int32
    """
    if not root:
        return []
    result = []

    def dfs(node, result):
        if node is None:
            return 0

        ht = max(dfs(node.left, result), dfs(node.right, result)) + 1
        if len(result) == ht - 1:
            result.append([])
        result[ht - 1].append(node.value)
        return ht

    dfs(root, result)
    return result

node_6 = BinaryTreeNode(6)
node_2 = BinaryTreeNode(2)
node_5 = BinaryTreeNode(5)
node_4 = BinaryTreeNode(4, node_6)
node_3 = BinaryTreeNode(3, node_4, node_5)
node_1 = BinaryTreeNode(1, node_2, node_3)
res = find_leaves(node_1)
print(res == [[2, 6, 5],[4],[3],[1]] or res == [[6, 2, 5], [4], [3], [1]] or res == [[2, 5, 6], [4], [3], [1]])

