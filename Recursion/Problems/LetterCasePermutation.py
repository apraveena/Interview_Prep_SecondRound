#leetcode 784
#Time complexity = O(n.2^n)
#with immutable parameter for slate as string, we are recreating the string everytime
#space complexity - implicit - call stack - O(n^2) - strings with partial solution co-exist on stack in memory
#space complexity - explicit= 2^n.n - results worst case
def ltr_case_permutation(s: str):
    result = []
    def helper(slate, s):
        if len(s) == 0:
            result.append(slate)
            return

        curr = s[0]
        if curr.isalpha():
            helper(slate + curr.lower(), s[1:])
            helper(slate + curr.upper(), s[1:])
        else:
            helper(slate + curr, s[1:])
    helper("", s)
    return result
#Time complexity = O(n.2^n)
#with immutable parameter for slate as string, we are recreating the string everytime
#space complexity - implicit - call stack - O(n^2) - strings with partial solution co-exist on stack in memory
#space complexity - explicit= 2^n.n - results worst case

def ltr_case_permutation1(s: str):
    result = []
    def helper(s, slate, i):
        if len(s) == i:
            result.append(slate)
            return

        curr = s[i]
        if curr.isdigit():
            helper(s, slate + curr, i + 1)
        else:
            helper(s, slate + curr.lower(), i + 1)
            helper(s, slate + curr.upper(), i + 1)

    helper(s, "", 0)
    return result

#We use mutable variable to keep appending and convert to immutable (string) variable
# when ready to append to the result
#space complexity - implicit - call stack - O(n)
#space complexity - explicit= 2^n.n
#Time complexity is still O(n.2^n)
def ltr_case_permutation_optimal(s: str):
    result = []
    def helper(s, slate, i):
        if len(s) == i:
            result.append("".join(slate))
            return

        curr = s[i]
        if curr.isdigit():
            slate.append(curr)
            helper(s, slate, i + 1)
            slate.pop()
        else:
            slate.append(curr.lower())
            helper(s, slate, i + 1)
            slate.pop()
            slate.append(curr.upper())
            helper(s, slate, i + 1)
            slate.pop()

    helper(s, [], 0)
    return result

print(ltr_case_permutation_optimal("a1b2"))