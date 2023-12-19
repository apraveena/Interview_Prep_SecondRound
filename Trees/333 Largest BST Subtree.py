def largestBSTSubtree(root):
    if root is None:
        return 0

    # Global problem: Find the largest BST subtree
    # Local (per-node) problem: Am I a BST? If yes, then how many nodes do I have?
    # Local -> Global: Global solution is the max of all local solutions which are BSTs
    # To calculate local solution, each node needs to figure out if it is a BST, and what is the number of nodes in its subtree
    #.... and also the largest element in the left subtree and the smallest int he right subtree
    #So each node needs to return 1. its size 2. largest element 3. smallest element 4.Whether iis ia bst

    global_size = [0]
    def dfs(node):

        my_size = 1
        my_smallest, my_largest = node.val, node.val
        am_i_bst = True

        #Base case: Leaf Node
        if node.left is None and node.right is None:
            pass

        #Recursive case: Internal node
        if node.left is not None:
            (size, smallest, largest, is_bst) = dfs(node.left)
            my_size += size
            my_smallest = min(my_smallest, smallest)
            my_largest = max(my_largest, largest)
            if not is_bst or largest >= node.val:
                am_i_bst = False

        if node.right is not None:
            (size, smallest, largest, is_bst) = dfs(node.right)
            my_size += size
            my_smallest = min(my_smallest, smallest)
            my_largest = max(my_largest, largest)
            if not is_bst or node.val >= smallest:
                am_i_bst = False

        if am_i_bst and my_size > global_size[0]:
            global_size[0] = my_size

        return my_size, my_smallest, my_largest, am_i_bst

    dfs(root)
    return global_size[0]


def find_largest_bst(root):
    if not root:
        return 1
    globalSize = [0]

    def dfs_helper(node):
        smallest = node.value
        largest = node.value
        #amibst should be True by default. If there is a problem, we set it to True, otherwise there is no way for it to be true
        amibst = True
        mySize = 1

        if node.left:
            (m, s, l, b) = dfs_helper(node.left)
            mySize = m + 1
            smallest = min(s, smallest)
            largest = max(l, largest)
            if not b or node.value < l:
                amibst = False

        if node.right:
            (m,s, l, b) = dfs_helper(node.right)
            mySize = m+1
            smallest = min(s, smallest)
            largest = max(l, largest)
            if not b or node.value > s:
                amibst = False

        if amibst and mySize > 0:
            globalSize[0] = max(mySize, globalSize[0])
        return (mySize,smallest, largest, amibst)

    dfs_helper(root)
    return globalSize[0]