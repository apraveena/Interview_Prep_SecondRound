#Using recursion so as to enable generic number sum called k_sum
#If not for generic, we could add another for loop for 3 sum for 4 sum calculation
def four_sum(a, target):
    a.sort()
    result, curr_list = [], []
    def helper(k, start, target):
        if k != 2:
            for i in range(start, len(a) - k + 1):
                if i > start and a[i] == a[i - 1]:
                    continue
                # target = target - a[i]
                curr_list.append(a[i])
                helper(k-1, i + 1, target-a[i])
                curr_list.pop()
            return
        l = start
        r = len(a) - 1
        while l < r:
            curr_sum = a[l] + a[r]
            if curr_sum > target:
                r -= 1
            elif curr_sum < target:
                l += 1
            else:
                result.append(curr_list + [a[l], a[r]])
                l += 1
                while a[l] == a[l-1] and l < r:
                    l += 1

    helper(4, 0, target)
    return result

#Copied from test code file, not sure if it works. above one should work.
def four_sum1(arr, target):
    """
    Args:
     arr(list_int32)
     target(int32)
    Returns:
     list_list_int32
    """
    curr_list, result = [], []
    arr.sort()

    # k is the size of the inner list to be returned
    # for four_sum, k= 4
    def ksum(start, target, k):
        if k != 2:
            for i in range(start, len(arr) - k + 1):
                if i > start and arr[i] == arr[i - 1]:
                    continue
                curr_list.append(arr[i])
                ksum(i + 1, target - arr[i], k - 1)
                curr_list.pop()
            return
        # Handle  2 sum here
        left, right = start, len(arr) - 1
        while left < right:
            subtotal = arr[left] + arr[right]
            if subtotal > target:
                right -= 1
            elif subtotal < target:
                left += 1
            else:
                result.append(curr_list + [arr[left], arr[right]])
                left += 1
                while arr[left] == arr[left - 1] and left < right:
                    left += 1

    ksum(0, target, 4)
    return result

list1 = [0, 0, 1, 3, 2, -1]
list1 = [0, 0, 1, 3]
print(four_sum1(list1, 2))


lst1 =  [0, 0, 1, 3, 2, -1]
target = 3
lst1 =  [100000, -99999, 1, 0, -99997, -1, -100000, 2]
lst1 =  [100, -99, 1, 0, -97, -1, -100, 2]
target = 2
# lst1 =  [-100000, -100000, -4, -100000, -99996, -100000, -100000]
# lst1 =  [1, 0, -99997, -1, -100000, 2]
target = -400000
print(four_sum(lst1, target))