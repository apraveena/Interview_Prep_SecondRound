class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
#ik top attemp 4th code
def construct_binary_tree(inorder, preorder):
    if len(inorder) == 0:
        return None
    preorder.reverse()
    lookup = {val:i for i, val in enumerate(inorder)}
    def helper(left, right):
        if left > right:
            return None
        node = BinaryTreeNode(preorder.pop())
        mid = lookup[node.value]
        node.left = helper(left, mid-1)
        node.right = helper(mid+1, right)
        return node
    return helper(0, len(inorder)-1)

#eg:
preorder = [10, 4, 2, 8, 14, 12, 17]
inorder = [2, 4, 8, 10, 12, 14, 17]
