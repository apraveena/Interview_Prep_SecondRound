#T(n) = n x 2 ^ n (same as others)
#Space complexity = 2 ^ n
def binary_strings_recursive_bfs(n):
    def helper(n):
        if n == 1:
            return(["0", "1"])

        prev = helper(n-1)
        result = []
        for item in prev:
            result.append(item + "0")
            result.append(item + "1")
        return result

    return helper(n)

#T(n) = n x 2 ^ n (same as others)
#Space complexity = 2 ^ n
def binary_strings_iterative_bfs(n):
    result = ["0", "1"]
    for i in range(2, n+1):
        new_result = []
        for item in result:
            new_result.append(item + "0")
            new_result.append(item + "1")
        result = new_result
    return result

#This is the recommended way - with partial solution(slate) and divide and conquer approach
#T(n) = n x 2 ^ n (same as others)
#Space complexity = O(n)
def binary_strings_recursive_dfs(n):
    result = []
    def helper(slate, n):
        if n == 0:
            result.append(slate)
        else:
            helper("0" + slate, n-1)
            helper("1" + slate, n-1)
    helper("", n)
    return result

print(binary_strings_recursive_dfs(3))

