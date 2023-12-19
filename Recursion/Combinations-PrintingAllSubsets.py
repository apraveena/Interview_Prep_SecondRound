def count_all_subsets(arr):
    result = []
    def helper(slate, arr):
        if len(arr) == 0:
            result.append(slate)
            return
        helper(slate, arr[1:])
        helper(slate + str(arr[0]), arr[1:])

    helper("", arr)
    return result


def generate_all_subsets_string(s):
    """
    Args:
     s(str)
    Returns:
     list_str
    """
    result = []
    def helper(slate, s):
        if len(s) == 0:
            result.append(slate)
            return

        helper(slate, s[1:])
        helper(slate + str(s[0]), s[1:])

    helper("", s)
    return result

lst1 = [1, 2, 3]
# lst1 = "xy"
print(generate_all_subsets_string(lst1))
