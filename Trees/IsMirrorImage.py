def mirror_image(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     Nothing
    """
    # Write your code here.
    root = mirror_image_util(root)
    return root


def mirror_image_util(root):
    if (root == None):
        return root

    left = mirror_image_util(root.left)
    right = mirror_image_util(root.right)

    # Swap the left and right pointers.
    root.left = right
    root.right = left
    return root