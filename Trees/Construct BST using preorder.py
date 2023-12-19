"""
For your reference:
"""
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

#from ik Tree class problems
#failed some cases
def build_binary_search_tree(pre_order):
    """
    Args:
     preorder(list_int32)
    Returns:
     BinaryTreeNode_int32
    """

    if pre_order is None:
        return pre_order

    in_order = pre_order[:]
    in_order.sort()

    def helper(p_start, p_end, i_start, i_end):

        if i_start > i_end:
            return None

        if i_start == i_end:
            return BinaryTreeNode(in_order[i_start])

        root_val = pre_order[p_start]
        root = BinaryTreeNode(root_val)

        i_idx = in_order.index(root_val)
        left_count = i_idx - i_start
        root.left = helper(p_start + 1, p_start + left_count, i_start, i_idx - 1)
        root.right = helper(p_start + left_count + 1, p_end, i_idx + 1, i_end)

        return root

    return helper(0, len(in_order) - 1, 0, len(in_order) - 1)
