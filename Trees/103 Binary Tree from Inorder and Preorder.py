from typing import List

class BinaryTreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def construct_binary_tree_from_inorder_and_preorder(inorder: List[int], preorder: List[int]):

    def helper(p_start, p_end, i_start, i_end):
        if i_start > i_end:
            return None
        if i_start == i_end:
            return BinaryTreeNode(inorder[i_start])

        root_val = preorder[p_start]
        root = BinaryTreeNode(root_val)

        i_idx = inorder.index(root_val)
        left_count = i_idx - i_start
        root.left = helper(p_start + 1, p_start + left_count, i_start, i_idx - 1)
        root.right = helper(p_start + left_count + 1, p_end, i_idx + 1, i_end)

        return root


    return helper(0, len(inorder)-1, 0, len(inorder)-1)


def test_bst_from_lists():
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    print(construct_binary_tree_from_inorder_and_preorder(inorder, preorder) == [3,9,20,None,None,15,7])