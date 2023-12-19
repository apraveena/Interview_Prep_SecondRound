def generate_poss_expr_to_sum_target(s, target):
    """
    Args:
     s(str)
     target(int64)
    Returns:
     list_str
    """
    result = []

    def my_eval(s):
        if len(s) == 0:
            return 0
        rem = []
        plus_list = s.split("+")
        for val1 in plus_list:
            res_plus = 0
            if "*" in val1:
                res_mult = 1
                mult_elems = val1.split("*")
                for mult_val in mult_elems:
                    res_mult = res_mult * int(mult_val)
                rem.append(res_mult)
            else:
                rem.append(int(val1))
        for plus_val in rem:
            res_plus = res_plus + plus_val

        return res_plus

    def helper(slate, i):

        if i == len(s):
            str1 = "".join(slate)
            res = my_eval(str1)
            if res == target:
                result.append(str1)
            return

        slate.append(s[i])
        helper(slate, i + 1)
        slate.pop()

        slate.append("+")
        slate.append(s[i])
        helper(slate, i + 1)
        slate.pop()
        slate.pop()

        slate.append("*")
        slate.append(s[i])
        helper(slate, i + 1)
        slate.pop()
        slate.pop()

    helper([s[0]], 1)
    return result




# print(my_eval("2+0*20+3*2+4+44+6"))
# print(my_eval("2+0+2"))
print(generate_poss_expr_to_sum_target("202", 4))