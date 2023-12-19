def power_iter(a, b):
    mod = 10 ** 8 + 7
    result = 1
    a = a % mod
    for i in range(b):
        result = (result * a) % mod
    return result % mod

def power_recursive(a, b):
    if b == 0: return 1
    mod = 10 ** 8 + 7
    a = a % mod
    return (a * power_recursive(a, b-1)) % mod

def power_iter_optimal(a, b):
    if b == 0: return 1

    mod = 10 ** 8 + 7
    result = 1
    a = a % mod
    while b > 0:
        if b % 2 == 1:
            result = (result * a) % mod
        a = a ** 2
        b = b // 2

    return result % mod

def power_recursive_optimal(a, b):
    if b == 0: return 1
    mod = 10 ** 8 + 7
    a = a % mod
    temp = power_recursive_optimal(a, b//2)
    temp = temp % mod
    temp = (temp * temp) % mod
    if b % 2 == 0:
        return temp
    else:
        return (a * temp) % mod

print(power_iter(100000000000000000000, 15))
print(power_iter(2, 5))
print(power_recursive(100000000000000000000, 15))
print(power_recursive(2, 5))
print(power_iter_optimal(100000000000000000000, 15))
print(power_iter_optimal(2, 5))
print(power_recursive_optimal(100000000000000000000, 15))
print(power_recursive_optimal(2, 5))
