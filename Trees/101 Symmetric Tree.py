#For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def check_symmetric(root):
    def helper(node1, node2):
        if not node1 and not node2:
            return True
        if not node1 or not node2:
            return False

        if node1.value == node2.value:
            return helper(node1.left, node2.right) and helper(node1.right, node2.left)

        return False
    return helper(root, root)


#Test case 1
node_70_left = BinaryTreeNode(70)
node_60_left = BinaryTreeNode(60)
node_90_left = BinaryTreeNode(90)
node_90_left.left = node_70_left
node_90_left.right = node_60_left

node_70_right = BinaryTreeNode(70)
node_60_right = BinaryTreeNode(60)
node_90_right = BinaryTreeNode(90)
node_90_right.left = node_60_right
node_90_right.right = node_70_right

node_100_root = BinaryTreeNode(100)
node_100_root.left = node_90_left
node_100_root.right = node_90_right

print(check_symmetric(node_100_root))

#Test case 2
node_7_left = BinaryTreeNode(7)
node_7_right = BinaryTreeNode(7)
node_5_left = BinaryTreeNode(5)
node_5_left.left = node_7_left
node_5_right = BinaryTreeNode(5)
node_5_right.right = node_7_right
node_root_1 = BinaryTreeNode(1)
node_root_1.left = node_5_left
node_root_1.right = node_5_right

print(check_symmetric(node_root_1))



