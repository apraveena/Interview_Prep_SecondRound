#if input array is [3, 5, 6]
#output expectation is [333, 356, 355, 366, 365, 335, 336,363, 353, ..] = 27 permutations
#if input array is [0, 1]
#output expectation is [00, 01, 10, 11] = 4 permutations
#time complexity = n. n ^ n? because n ^ n permutations with repetitions allowed and n to append slate to the result
def permutations_repetitions_allowed(arr):
    result = []
    def helper(slate):
        if len(slate) == len(arr):
            result.append("".join(slate))
            return

        for j in range(len(arr)):
            slate.append(str(arr[j]))
            helper(slate)
            slate.pop()

    helper([])
    return result


lst1 = [0, 1]
lst2 = [3, 5, 6]
lst3 = ["x", "c", "m"]
print(lst1)
print(lst2)
print(lst3)
print("\n--------Permutations repetitions allowed--------------")
res1 = permutations_repetitions_allowed(lst1)
print(f"Length: {len(res1)} Result: {res1})")
res2 = permutations_repetitions_allowed(lst2)
print(f"Length: {len(res2)} Result: {res2})")
res3 = permutations_repetitions_allowed(lst3)
print(f"Length: {len(res3)} Result: {res3})")

#if input array is [3, 5, 6]
#output expectation is [356, 365, 536, 563, 653, 635] = 6 permutations
#if input array is [0, 1]
#output expectation is [01, 10] = 2 permutations
#If repetitions are not allowed, I will send a subproblem instead of iterating over all the items
#in the main array
#Time complexity = n!. n
def permutations_repetitions_not_allowed(arr):
    result = []
    def helper(slate, sub_problem):
        if len(slate) == len(arr):
            result.append("".join(slate))
            return

        for idx in range(len(sub_problem)):
            slate.append(str(sub_problem[idx]))
            helper(slate, sub_problem[:idx] + sub_problem[idx+1:])
            slate.pop()

    helper([], arr)
    return result

print("\n--------Permutations repetitions not allowed--------------")
res1 = permutations_repetitions_not_allowed(lst1)
print(f"Length: {len(res1)} Result: {res1})")
res2 = permutations_repetitions_not_allowed(lst2)
print(f"Length: {len(res2)} Result: {res2})")
res3 = permutations_repetitions_not_allowed(lst3)
print(f"Length: {len(res3)} Result: {res3})")

#if input array is [3, 5, 6]
#output expectation is [356] = 1 combination since 356 is same 653 same as 365 etc..
# order matters.. repeating the same combination in different order is considered duplicate
#if input array is [0, 1]
#output expectation is [01] = 1 combination since 01 is same as 10
# and repetitions dont make sense in combinations
#eg: 3 students are forming a committee.. we cannot repeat a student
#Time complexity = O(n)?
def combinations(arr):
    result = []
    def helper(slate, i):
        if len(slate) == len(arr):
            result.append("".join(slate))
            return

        slate.append(str(arr[i]))
        helper(slate, i+1)
        slate.pop()

    helper([], 0)
    return result

print("\n--------combinations--------------")
res1 = combinations(lst1)
print(f"Length: {len(res1)} Result: {res1})")
res2 = combinations(lst2)
print(f"Length: {len(res2)} Result: {res2})")
res3 = combinations(lst3)
print(f"Length: {len(res3)} Result: {res3})")

#if input array is [3, 5, 6] and k is 2
#output expectation is [356] = [35, 56, 36] - 3 combinations 3!/(2!.1!)
#if input array is [0, 1] and k is 1
#output expectation is [0, 1] = 2 combinations 2 choose 1 = 2!/(1!.1!)
#we can use strategy of include and exclude for each element
#instead of for loop, take each item and include or exclude that element and call with
#rest of the array (sub problem)
#Time complexity O(n) = n . n choose k?
def combinations_choose_k(arr, k):
    result = []
    def helper(slate, sub_problem, n):
        if len(slate) == k:
            result.append("".join(slate))
            return

        if n == 0:
            return

        #include case
        slate.append(str(sub_problem[0]))
        helper(slate, sub_problem[1:], n-1)
        slate.pop()

        #exclude case
        helper(slate, sub_problem[1:], n-1)

    helper([], arr, len(arr))
    return result

print("\n--------combinations - n choose k--------------")
res1 = combinations_choose_k(lst1, 1)
print(f"Length: {len(res1)} Result: {res1})")
res2 = combinations_choose_k(lst2, 2)
print(f"Length: {len(res2)} Result: {res2})")
res3 = combinations_choose_k(lst3, 2)
print(f"Length: {len(res3)} Result: {res3})")

#if input array is [3, 5, 6]
#output expectation is [356] = [356, 35, 36, 56, 3, 5, 6, ''] - 8 combinations 2^n = 2^3 = 8
#if input array is [0, 1]
#output expectation is [0, 1] = 4 combinations = [01, 1, 0, ""]
#Similar to n choose k, but this time we go all the way till the subproblem is empty
#Time complexity = O(n) = n. 2  ^ n?
def combinations_subsets_powerset(arr):
    result = []
    def helper(slate, sub_problem):
        if len(sub_problem) == 0:
            result.append("".join(slate))
            return

        #include case
        slate.append(str(sub_problem[0]))
        helper(slate, sub_problem[1:])
        slate.pop()

        #exclude case
        helper(slate, sub_problem[1:])

    helper([], arr)
    return result

print("\n--------subsets--------------")
res1 = combinations_subsets_powerset(lst1)
print(f"Length: {len(res1)} Result: {res1})")
res2 = combinations_subsets_powerset(lst2)
print(f"Length: {len(res2)} Result: {res2})")
res3 = combinations_subsets_powerset(lst3)
print(f"Length: {len(res3)} Result: {res3})")

