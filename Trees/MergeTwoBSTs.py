"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def merge_two_binary_search_trees(root1, root2):
    """
    Args:
     root1(BinaryTreeNode_int32)
     root2(BinaryTreeNode_int32)
    Returns:
     BinaryTreeNode_int32
    """
    if not root1 and not root2:
        return None

    if not root1:
        return root2

    if not root2:
        return root1

    arr1, arr2, merged_arr = [], [], []

    def build_arr_with_bst(node, arr):
        if node.left:
            build_arr_with_bst(node.left, arr)
        arr.append(node.value)
        if node.right:
            build_arr_with_bst(node.right, arr)

    build_arr_with_bst(root1, arr1)
    build_arr_with_bst(root2, arr2)

    def build_BST(arr, start, end):
        if start > end:
            return None

        mid = start + (end - start) // 2
        root = BinaryTreeNode(arr[mid])
        root.left = build_BST(arr, start, mid - 1)
        root.right = build_BST(arr, mid + 1, end)

        return root

    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            merged_arr.append(arr1[i])
            i += 1
        else:
            merged_arr.append(arr2[j])
            j += 1

    while i < len(arr1):
        merged_arr.append(arr1[i])
        i += 1

    while j < len(arr2):
        merged_arr.append(arr2[j])
        j += 1

    return build_BST(merged_arr, 0, len(merged_arr) - 1)


'''
Suneetha's code
'''



