class Solution:
    from typing import List
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        hm = {ltr: i for i, ltr in enumerate(order)}
        for i in range(len(words) - 1):
            first_word, second_word = words[i], words[i + 1]
            # j, k are pointers to first_word and second_word
            j = 0
            broke_out = False
            while j < len(first_word) and j < len(second_word):
                if first_word[j] != second_word[j]:  # mismatch
                    if hm[first_word[j]] > hm[second_word[j]]:
                        return False
                    broke_out = True
                    break
                j += 1

            if not broke_out and j < len(first_word):
                return False

        return True

sln = Solution()
print(sln.isAlienSorted(["fxasxpc","dfbdrifhp","nwzgs","cmwqriv","ebulyfyve","miracx","sxckdwzv","dtijzluhts","wwbmnge","qmjwymmyox"], "zkgwaverfimqxbnctdplsjyohu") == False)
print(sln.isAlienSorted(["app","apple"], "hlabcdefgijkmnopqrstuvwxyz") == True)
print(sln.isAlienSorted(["apple","app"], "hlabcdefgijkmnopqrstuvwxyz") == False)
# print(sln.isAlienSorted(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz") == True)
from typing import List
def isAlienSorted(self, words: List[str], order: str) -> bool:
    orderIdx = {ch: i for i, ch in enumerate(order)}
    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]
        for j in range(len(w1)):
            if j == len(w2):
                return False
            if w1[j] != w2[j]:
                if orderIdx[w2[j]] < orderIdx[w1[j]]:
                    return False
                break
    return True


# words = ["word","world","row"]
# order ="worldabcefghijkmnpqstuvxyz"
words = ["hello", "leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"
s = Solution()
# print(s.isAlienSorted(words, order) == True)
