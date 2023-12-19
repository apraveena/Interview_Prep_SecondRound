# Libraries Included:
# Numpy, Scipy, Scikit, Pandas

'''
Given the root of a binary tree with unique values and the values of two different nodes of the tree x and y,
return true if the nodes corresponding to the values x and y in the tree are cousins, or false otherwise.
Two nodes of a binary tree are cousins if they have the same depth with different parents.
Note that in a binary tree, the root node is at the depth 0, and children of each depth k node are at the depth k + 1.

'''

def are_cousins(root, x, y):
    if not root:
        return False

    global parent_x, parent_y, depth_x, depth_y, found_x, found_y
    parent_x, parent_y, depth_x, depth_y = None, None, 0, 0

    def dfs(node, x, y, depth, parent):
        global parent_x, parent_y, depth_x, depth_y, found_x, found_y
        found_x, found_y = False, False

        if node.value == x:
            parent_x = parent
            depth_x = depth
            found_x = True

        if node.value == y:
            parent_y = parent
            depth_y = depth
            found_y = True

        #backtracking
        if found_x and found_y:
            return

        # recursive case
        if node.left:
            dfs(node.left, x, y, depth + 1, node)

        if node.right:
            dfs(node.right, x, y, depth + 1, node)

    dfs(root, x, y, 0, None)
    if found_x and found_y:
        return depth_x == depth_y and parent_x.value != parent_y.value

    return False




