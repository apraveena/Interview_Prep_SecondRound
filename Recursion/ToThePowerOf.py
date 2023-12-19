def raise_to_the_power_of_rec(n, k):
    if k == 0:
        return 1
    return n * raise_to_the_power_of_rec(n, k-1)

def raise_to_the_power_of_iter(n, k):
    result = 1
    for i in range(k):
        result *= n

    return result

print(raise_to_the_power_of_rec(2, 8))
print(raise_to_the_power_of_iter(2, 8))

