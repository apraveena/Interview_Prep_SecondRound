def get_distinct_subsets(s):
    """
    Args:
     s(str)
    Returns:
     list_str
    """
    result = []

    # str_list = []
    # for x in s:
    #     str_list.append(x)

    str_lst = [x for x in s]
    str_lst.sort()
    print(str_lst)
    def helper(slate, i):

        if i == len(s):
            str_slate = "".join(slate)
            if str_slate not in result:
                result.append(str_slate)
            return

        slate.append(str_lst[i])
        helper(slate, i + 1)
        slate.pop()

        helper(slate, i + 1)

    helper([], 0)
    return result

print(get_distinct_subsets("dc"))