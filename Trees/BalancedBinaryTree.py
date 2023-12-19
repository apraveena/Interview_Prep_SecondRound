def is_height_balanced(root):
    def balanced(node):
        if node == None:
            return (0, True)

        left_result = balanced(node.left)
        right_result = balanced(node.right)

        left_height = left_result[0]
        right_height = right_result[0]

        left_balanced = left_result[1]
        right_balanced = right_result[1]

        self_balanced = True

        if abs(left_height - right_height) > 1:
            self_balanced = False

        if not left_balanced or not right_balanced:
            self_balanced = False

        return (max(left_height, right_height) + 1, self_balanced)

    result = balanced(root)

    return result[1]