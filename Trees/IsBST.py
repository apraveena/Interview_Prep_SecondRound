class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def is_it_bst(root):
    if not root:
        return True
    def helper(node):
        if not node:
            return
        is_bst = True
        if node.left:
            is_bst = helper(node.left) and is_bst
            if not is_bst: return False

        if node.right:
            is_bst = helper(node.right) and is_bst
            if not is_bst: return False

        return is_bst


"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
#worked in ik ide

def is_bst(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     bool
    """
    global is_tree_bst
    if root is None:
        return True

    is_tree_bst = True

    def dfs(node):
        global is_tree_bst

        am_i_bst, smallest, largest = True, node.value, node.value

        # Recursive case: Internal node
        if node.left:
            b, s, l = dfs(node.left)
            smallest = min(smallest, s)
            largest = max(largest, l)
            if not b or l > node.value:
                am_i_bst = False

        if node.right:
            b, s, l = dfs(node.right)
            smallest = min(smallest, s)
            largest = max(largest, l)
            if not b or s < node.value:
                am_i_bst = False

        if am_i_bst == False:
            is_tree_bst = False

        return am_i_bst, smallest, largest

    dfs(root)
    return is_tree_bst
'''Suneetha code - modified'''
"""
For your reference:
"""
class BinaryTreeNode:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

def is_bst_Suneetha(root):
    if not root:
        return True
    is_BST = [True]

    def dfs_helper(node):
        smallest = node.value
        largest = node.value
        #amibst should be True by default. If there is a problem, we set it to True, otherwise there is no way for it to be true
        amibst = True

        # leaf node
        #Praveena: There is no need for this code, this doesn't do anything. Can delete
        if node.left == None and node.right == None:
            pass

        if node.left:
            (s, l, b) = dfs_helper(node.left)
            smallest = min(s, smallest)
            largest = max(l, largest)
            # now i need to find out wether i am bst or not
            #Praveena: need to compare with l, not largest otherwise the node could be checking with itself
            #Praveena: Also, the comparison symbols were reversed
            #Praveena: Also, for whatever reason, ik tool thinks it's ok to have same node value in parent and child,
            # so get rid of = sign. node.value < l: is enough
            if not b or node.value < l:
                amibst = False

        if node.right:
            (s, l, b) = dfs_helper(node.right)
            smallest = min(s, smallest)
            largest = max(l, largest)
            # Praveena: need to compare with s, not smallest otherwise the node could be checking with itself
            # Praveena: Also, the comparison symbols were reversed
            # Praveena: Also, for whatever reason, ik tool thinks it's ok to have same node value in parent and child,
            # so get rid of = sign. node.value > s: is enough
            if not b or node.value > s:
                amibst = False

        if amibst == False:
            is_BST[0] = False
        return (smallest, largest, amibst)

    dfs_helper(root)
    return is_BST[0]

node_7 = BinaryTreeNode(7)
node_4 = BinaryTreeNode(4)
node_5 = BinaryTreeNode(5, node_4, node_7)

print(is_bst_Suneetha(node_5))
