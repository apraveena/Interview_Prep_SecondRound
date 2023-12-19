def factorial_recursive(n):
    if n in (0, 1):
        return n
    return n * factorial_recursive(n-1)

def factorial_iterative(n):
    #bottom up
    fact = 1
    for i in range(2, n+1):
        fact *= i
    return fact

print(factorial_recursive(5))
print(factorial_iterative(5))