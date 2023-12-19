class Solution:
    def numSplits(self, s: str) -> int:
        if len(s) < 2:
            return 0

        left = [0] * 26
        right = [0] * 26

        right_unique = 0
        left_unique = 0

        equal = 0

        # Store frequency of characters
        for i in s:
            if right[ord(i) - ord('a')] == 0:
                right_unique += 1
            right[ord(i) - ord('a')] += 1

        #Find frequency of characters in left and right substring
        for i in s:
            if left[ord(i) - ord('a')] == 0:
                left_unique += 1

            left[ord(i) - ord('a')] += 1
            right[ord(i) - ord('a')] -= 1

            if right[ord(i) - ord('a')] == 0:
                right_unique -= 1

            if left_unique == right_unique:
                equal += 1

        return equal