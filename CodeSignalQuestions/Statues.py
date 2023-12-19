def remaining_statues(statues):
    count_list = [0] * 21
    final = []

    for statue in statues:
        count_list[statue] = 1

    left, right = 0, 20
    found = False
    while not found:
        while count_list[left] == 0:
            left += 1

        while count_list[right] == 0:
            right -= 1

        for i in range(left, right + 1):
            if count_list[i] == 0:
                final.append(i)
            found = True

    return len(final)

print(remaining_statues([6, 2, 3, 8]) == 3) #[4, 5, 7]


