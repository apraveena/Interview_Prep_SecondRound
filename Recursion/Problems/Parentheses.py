#leetcode 22

def parenthesis(n):
    result = []
    #op = remaining open parentheses
    #cl = remaining close parentheses
    def helper(slate, op, cl):
        if op > cl:
            return

        if op < 0 or cl < 0:
            return

        if op == 0 and cl == 0:
            result.append("".join(slate))
            return

        slate.append("(")
        helper(slate, op-1, cl)
        slate.pop()

        slate.append(")")
        helper(slate, op, cl-1)
        slate.pop()

    helper([], n, n)
    return result


print(parenthesis(3))