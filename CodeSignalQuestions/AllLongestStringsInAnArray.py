def solution(inputArray):
    count_list = [[] for i in range(10)]
    for strng in inputArray:
        count = len(strng)
        count_list[count-1].append(strng)

    for i in range(9, -1, -1):
        if not len(count_list[i]) == 0:
            return count_list[i]

def solution(inputArray):
    m = max(len(s) for s in inputArray)
    r = [s for s in inputArray if len(s) == m]
    return r

# print(solution( ["aba", "aa", "ad", "vcd", "aba"]) == ["aba", "vcd", "aba"])
print(solution( ["young",
 "yooooooung",
 "hot",
 "or",
 "not",
 "come",
 "on",
 "fire",
 "water",
 "watermelon"]) == ["yooooooung", "watermelon"])