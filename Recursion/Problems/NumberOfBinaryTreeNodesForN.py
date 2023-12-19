def how_many_bsts(n):
    # if n in (0, 1):
    #     return 1
    # count = 0
    # for i in range(1, n+1):
    #     count = count + how_many_bsts(i-1) * how_many_bsts(n-i)
    # return count
    count = 0
    if n in (1, 0):
        return 1
    for i in range(1, n+1):
        #when i is root
        count = count + how_many_bsts(i-1) * how_many_bsts(n-i)

    return count


print(how_many_bsts(1))
print(how_many_bsts(2))
print(how_many_bsts(3))
print(how_many_bsts(4))