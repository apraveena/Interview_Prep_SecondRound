def solution(s1, s2):
    com = [min(s1.count(i), s2.count(i)) for i in set(s1)]
    return sum(com)

#eg: 1. fried, freed 2. maple, apple 3. forty, toons
def solution(s1, s2):
    s1count, s2count, common = 0, 0, 0
    set_s1 = set(s1)
    for str1 in set_s1:
        s1_count = s1.count(str1)
        s2_count = s2.count(str1)
        common += min(s1_count, s2_count)
    return common
from collections import Counter

def solution(s1, s2):
    counter1 = Counter(s1)
    counter2 = Counter(s2)

    intersection = counter1 & counter2

    return sum(intersection.values())
