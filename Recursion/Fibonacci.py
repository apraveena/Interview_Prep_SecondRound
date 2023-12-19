#T(n) = O(2^n) aux space = O(n)
def fib_recursive(n):
    if n == 0 or n == 1:
        return n
    return fib_recursive(n-1) + fib_recursive(n-2)

#memoized version of recursive way
# T(n) = O(n) space = O(n)
def fib_recursive_memoized(n):
    if n in (0, 1):
        return n

    dp = [-1] * (n+1)
    dp[1] = 1
    dp[0] = 0
    def helper(n):
        if dp[n] != -1:
            return dp[n]
        x = helper(n-1)
        y = helper(n-2)
        dp[n] = helper(n-1) + helper(n-2)
    helper(n)
    return dp[n]

#iterative dynamic programming
#T(n) = O(n), space = O(n)
def fib_iterative(n):
    if n in (0, 1):
        return n
    dp = [-1] * (n + 1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

#T(n)=O(n), space = O(1)
def fib_space_optimized_iterative(n):
    if n in (0, 1):
        return n
    super_prev, prev = 0, 1
    for i in range(2, n + 1):
        temp = prev + super_prev
        super_prev = prev
        prev = temp
    return temp

f = lambda x: fib_space_optimized_iterative(x)
print(f(1)) #1
print(f(2)) #1
print(f(3)) #2
print(f(4)) #3
print(f(5)) #5
print(f(6)) #8