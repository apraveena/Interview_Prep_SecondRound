"""
For your reference:
"""
class BinaryTreeNode:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

#works but ik wants the output in different order
def vertical_order_traversal_dfs(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     list_list_int32
    """
    if not root:
        return 0
    hmap = {}
    result = []
    def dfs(node, hmap, dist):
        if node.left:
            dist -= 1
            dfs(node.left, hmap, dist)
            dist += 1

        if dist in hmap:
            hmap[dist].append(node.value)
        else:
            hmap[dist] = [node.value]

        if node.right:
            dist += 1
            dfs(node.right, hmap, dist)
            dist -= 1

    dfs(root, hmap, 0)
    for dist, value_list in hmap.items():
        temp = []
        for val in value_list:
            temp.append(val)
        result.append(temp[:])

    return result

node_4 = BinaryTreeNode(4)
node_5 = BinaryTreeNode(5)
node_6 = BinaryTreeNode(6)
node_8 = BinaryTreeNode(8)

node_7 = BinaryTreeNode(7, node_8)
node_2 = BinaryTreeNode(2, node_4, node_5)
node_3 = BinaryTreeNode(3, node_6, node_7)
node_1 = BinaryTreeNode(1, node_2, node_3)

print(vertical_order_traversal_dfs(node_1))

