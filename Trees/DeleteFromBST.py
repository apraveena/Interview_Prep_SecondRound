"""
For your reference:
"""
class BinaryTreeNode:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right


"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""


def delete_from_bst(root, values_to_be_deleted):
    """
    Args:
     root(BinaryTreeNode_int32)
     values_to_be_deleted(list_int32)
    Returns:
     BinaryTreeNode_int32
    """

    def delete(root, value):
        if root is None:
            return root

        curr = root
        prev = None
        while curr is not None:
            if value < curr.value:
                prev = curr
                curr = curr.left
            elif value > curr.value:
                prev = curr
                curr = curr.right
            else:
                break
        if curr is None:
            return root

        # Case 1: node has no children
        if curr.left is None and curr.right is None:
            # There must have been only one element in the tree
            # We want to delete that as well
            if prev == None:
                return None
            if curr == prev.left:
                prev.left = None
            else:
                prev.right = None

            return root

        # Case 2: node has 1 child
        # if we are here then curr has atleast one child
        if curr.left is None or curr.right is None:
            if curr.left is not None:
                child = curr.left
            else:
                child = curr.right
            # Removing root with children
            if prev is None:
                root = child
                return root

            if curr is prev.left:
                prev.left = child
            else:
                prev.right = child

            return root

        # Case 3: node has both children
        # find the successor by finding the min of the right tree
        # min value will be at far left in the right tree
        succ = curr.right
        prev = curr
        while succ.left is not None:
            prev = succ
            succ = succ.left

        curr.value = succ.value

        # we know successor has no right child since
        # the successor is supposed to be the leaf node
        if succ is prev.left:
            prev.left = succ.right
        else:  # succ is prev.right - wonder if this ever gets triggered
            prev.right = succ.right
        return root

    for value in values_to_be_deleted:
        root = delete(root, value)

    return root

def print_bst(root: BinaryTreeNode):
    def dfs(root: BinaryTreeNode):
        if root is None:
            return
        if root.left:
            dfs(root.left)
        print(root.value, end=" ")
        if root.right:
            dfs(root.right)

    dfs(root)
    print()
# #Make Test Data
# #4 is root, 2, 6 in level 1, 1, 3 are children of 2 and 5, 7 are children of 6
# node_1 = BinaryTreeNode(1)
# node_3 = BinaryTreeNode(3)
# node_5 = BinaryTreeNode(5)
# node_7 = BinaryTreeNode(7)
#
# node_2 = BinaryTreeNode(2, node_1, node_3)
# node_6 = BinaryTreeNode(6, node_5, node_7)
#
# node_4  = BinaryTreeNode(4, node_2, node_6)
# print_bst(node_4)
# lst1 = [5, 6]
# print(f"values to be deleted: {lst1}")
# res = delete_from_bst(node_4, lst1)
# print_bst(res)
#
# #4 is root, 2, 7 in level 1. 1, 3 are children of 2
# node_1 = BinaryTreeNode(1)
# node_3 = BinaryTreeNode(3)
# node_7 = BinaryTreeNode(7)
# node_2 = BinaryTreeNode(2, node_1, node_3)
# node_4  = BinaryTreeNode(4, node_2, node_7)
# print_bst(node_4)
# lst1 = [-1, 0, 8, 9]
# print(f"values to be deleted: {lst1}")
# res = delete_from_bst(node_4, lst1)
# print_bst(res)
# lst1 = [2]
# res = delete_from_bst(node_4, lst1)
# print_bst(res)

#4 is root, 2, 7 in level 1. 1, 3 are children of 2
node_neg_1 = BinaryTreeNode(-1)
node_5 = BinaryTreeNode(5)
node_3 = BinaryTreeNode(3, node_neg_1, node_5)
node_11 = BinaryTreeNode(11)
node_10  = BinaryTreeNode(10, node_3, node_11)
print_bst(node_10)
lst1 = [3, 6, 9]
print(f"values to be deleted: {lst1}")
res = delete_from_bst(node_10, lst1)
print_bst(res)
