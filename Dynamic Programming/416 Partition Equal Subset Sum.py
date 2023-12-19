#Copied from live class slide
def partition(nums):
    all_sum = sum(nums)
    if all_sum % 2 != 0:
        return False

    equal_sum = int(all_sum/2)

    # f(i, s) -> can I form subgroup from elements starting at the
    # ith element to the end whose subset sum is equal to s
    #
    # f(i, s) = f(i+1, s) OR f(i+1, s-nums[i])
    # answer -> f(0, target_sum)
    # Base cases ->
    # f(len(nums), 0) = True
    # f(len(nums), sum != 0) = False
    # f(any i, 0) = True

    #Initialization
    table = [[False] * (equal_sum + 1) for _ in range(len(nums) - 1)]

    for i in range(len(nums), -1, -1):
        for s in range(equal_sum + 1):
            #Base cases
            if s == 0:
                table[i][0] = True
                continue

            if i == len(nums):
                table[i][s] = False
                continue

            if s>= nums[i]:
                table[i][s] = table[i + 1][s - nums[i]]

            table[i][s] = table[i][s] or table[i + 1][s]

        return table[0][equal_sum]