def is_valid_bst(root):
    '''

    :param root: TreeNode
    :return: bool
    '''
    #Global problem: determine if the tree is BST
    #Local (per-node) problem: Determine if the subtree rooted at each node
    # is a bst
    #Local -> global: All local problems must return True for Global solution
    # to be True
    #So if any local solution is False, global will also become False
    if not root:
        return True

    isBST = [True]
    def dfs(node):
        # A node will determine if it is BST by looking at its left and right subtrees
        # The largest value in the left subtree should be smaller than the root value.
        # The smallest value in the right subtree should be larger than the root value.
        # So each node should return (smallest, largest, isbst) values in its subtree back to its parent

        am_i_bst = True
        smallest, largest = node.val, node.val

        #Base case: Leaf node
        if node.left is None and node.right is None:
            pass

        #Recursive case: Internal node
        if node.left is not None:
            (s, l, b) = dfs(node.left)
            smallest = min(smallest, s)
            largest = max(largest, s)
            if not b or l >= node.val:
                am_i_bst = False

        if node.right is not None:
            (s, l, b) = dfs(node.right)
            smallest = min(smallest, s)
            largest = max(largest, s)
            if not b or s <= node.val:
                am_i_bst = False

        if am_i_bst == False:
            isBST[0] = False

        return (smallest, largest, am_i_bst)

    dfs(root)
    return isBST[0] # or (S, L, B) = dfs(root); return B