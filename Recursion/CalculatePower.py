
















'''
 if b == 0:return 1
    a = a % mod
    tmp = calculate_power(a, b//2) % mod
    if b % 2 == 0:
        return (tmp * tmp) % mod
    else:
        return (a * tmp * tmp) % mod

'''