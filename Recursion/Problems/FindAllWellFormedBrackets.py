def find_all_well_formed_brackets(n):
    """
    Args:
     n(int32)
    Returns:
     list_str
    """
    result = []

    def helper(op, cl, slate):
        if op > cl or op < 0 or cl < 0:
            return

        if op == 0 and cl == 0:
            result.append("".join(slate))
            return

        # include open bracket
        slate.append("(")
        helper(op - 1, cl, slate)
        slate.pop()

        # include close bracket
        slate.append(")")
        helper(op, cl - 1, slate)
        slate.pop()

    helper(n, n, [])
    return result

print(find_all_well_formed_brackets(3))



