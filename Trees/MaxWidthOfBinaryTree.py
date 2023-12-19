
class BinaryTreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

from collections import deque
def find_maximum_width(root):
    # Trying again on my own
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     int32
    """
    if not root:
        return 0
    q = deque()
    q.append((root, 0))
    max_width = 1

    while q:
        left_most_idx, right_most_idx = q[0][1], q[0][1]
        for i in range(len(q)):
            curr_item = q.popleft()
            curr_node, curr_id = curr_item[0], curr_item[1]
            left_most_idx, right_most_idx = min(left_most_idx, curr_id), max(right_most_idx, curr_id)
            if curr_node.left: q.append((curr_node.left, 2 * curr_id + 1))
            if curr_node.right: q.append((curr_node.right, 2 * curr_id + 2))
        max_width = max(max_width, right_most_idx - left_most_idx + 1)
    return max_width

node_4 = BinaryTreeNode(4)
node_5 = BinaryTreeNode(5)
node_2 = BinaryTreeNode(2, node_4)
node_3 = BinaryTreeNode(3, node_5)
node_1 = BinaryTreeNode(1, node_2, node_3)

print(find_maximum_width(node_1))
