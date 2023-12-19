def insertion_sort(lst):
    for i in range(1, len(lst)):
        temp = lst[i]
        curr = i - 1
        while curr >= 0 and lst[curr] > temp:
            lst[curr + 1] = lst[curr]
            curr -= 1
        lst[curr + 1] = temp
    # return lst

lst1 = [8, 2, 4, 9, 3, 6]
lst1 = [2, 8, 4, 9, 3, 6]
lst1 = [2, 3, 4, 6, 8, 9]
lst1 = [9, 8, 6, 4, 3, 2]
# print(insertion_sort(lst1))
insertion_sort(lst1)
print(lst1)